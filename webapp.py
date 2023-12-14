from flask import Flask, render_template, request, redirect , session , jsonify
from flask_session import Session
from pymongo import MongoClient
from gridfs import GridFS
from main import *
from werkzeug.utils import secure_filename
import io
from PIL import Image
import os
import base64
import hashlib
from numberPlate import *
from pdf2image import convert_from_path
import fitz
from usecase1 import *
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
client = MongoClient('localhost', 27017)
db = client['textScanner']
collection = db.photoStore
fs=GridFS(db)


@app.route("/")
def home():
     return render_template("index.html", title="Home Page")


@app.route("/home")
def index():
    filename = session.get('filenames', '')
    print(filename)
    result = collection.find_one({"filename": filename[-1]})
    print(result['data'])
    print(type(result))
    image_stream = io.BytesIO(result['data'])
    img = Image.open(image_stream)
    image_np = np.array(img)
    # img.show(img)
    text=All.textExtract(image_np)
    lang=All.langDetect(text)
    return render_template("index.html",given=text,language=lang)
def calculate_imgbyte(imagef):
    im = Image.open(imagef)
    img_byte=io.BytesIO()
    im.save(img_byte , format='PNG')

    return img_byte.getvalue()

def calculate_hash(image_byte , filename):
    m = hashlib.sha256()
    m.update(image_byte)
    m.update(filename)

    return m.hexdigest()


def calculate_pdfbyte(pdf_path):
     # Convert the first page of the PDF to an image (you may adjust the page number)
    images = convert_from_path(pdf_path, first_page=1, last_page=1)
    # Convert the image to bytes
    byte_image = images[0].tobytes()
    return byte_image

@app.route("/upload",methods=['POST'])
def upload_image():
    try:
        imagef = request.files['fileUpload']
        filename = os.path.basename(imagef.filename)
        byte_image = calculate_imgbyte(imagef=imagef)
        hash = calculate_hash(byte_image , filename.encode())
        existing_document = collection.find_one({"image_hash": hash})

        if existing_document:
            # A document with the same filename already exists
            return jsonify({"message": "File with the same name already exists."}), 409 #, redirect('/') #---check
        
        filenames = session.get('filenames', [])
        filenames.append(filename)
        session['filenames'] = filenames
        image = {'data' :  byte_image, 'filename' : filename , 'image_hash' : hash}

        insert_result = collection.insert_one(image)

        if insert_result.inserted_id:
                # Data was inserted successfully
                return redirect('/home')
        else:
            # Data insertion failed
            return "Data insertion failed."
    except Exception as e:
         return str(e)
    

@app.route("/vehicle")
def vehicle():
    return render_template("vehicle.html",title="ExtractNumberplate")

@app.route("/uploadV",methods=['post'])
def uploadV():
    try:
        imagef = request.files['fileUpload']
        filename = os.path.basename(imagef.filename)
        byte_image = calculate_imgbyte(imagef=imagef)
        hash = calculate_hash(byte_image , filename.encode())
        existing_document = collection.find_one({"image_hash": hash})

        if existing_document:
            # A document with the same filename already exists
            return jsonify({"message": "File with the same name already exists."}), 409 #, redirect('/') #---check
        
        filenames = session.get('filenames', [])
        filenames.append(filename)
        session['filenames'] = filenames
        image = {'data' :  byte_image, 'filename' : filename , 'image_hash' : hash}

        insert_result = collection.insert_one(image)

        if insert_result.inserted_id:
                # Data was inserted successfully
                return redirect('/vehicleV')
        else:
            # Data insertion failed
            return "Data insertion failed."
    except Exception as e:
         return str(e)
@app.route('/vehicleV')
def vehicleV():
    filename = session.get('filenames', '')
    # print("Hello tis is Line1")
    # print(filename)
    result = collection.find_one({"filename": filename[-1]})
    # print(filename[-1])
    # print(result['data'])
    # print("Hello tis is Line2")
    # print(type(result))
    image_stream = io.BytesIO(result['data'])
    img = Image.open(image_stream)
    image_np = np.array(img)
    # img.show(img)

    text=nplate.extractNplate(image_np)
    # print(text)
    return render_template("vehicle.html",given=text)

@app.route("/Info")
def Info():
     
    return render_template("Info.html",title="Info Page Only")


@app.route("/pdfext")
def pdfext():
     
    return render_template("pdfext.html",title="ExtractPDF")


@app.route("/uploadP",methods=['post'])
def uploadP():
    try:
        pdf_path = request.files['fileUpload']  
        filename = secure_filename(pdf_path.filename)
        byte_pdf = pdf_path.read()
        hash = calculate_hash(byte_pdf, filename.encode())
        existing_document = collection.find_one({"pdf_hash": hash})

        if existing_document:
            # A document with the same filename already exists
            return jsonify({"message": "File with the same name already exists."}), 409

        filenames = session.get('filenames', [])
        filenames.append(filename)
        session['filenames'] = filenames
        pdf_document = {'data': byte_pdf, 'filename': filename, 'pdf_hash': hash}

        insert_result = collection.insert_one(pdf_document)

        if insert_result.inserted_id:
            # Data was inserted successfully
            return redirect('/extPdf')
        else:
            # Data insertion failed
            return "Data insertion failed."
    except Exception as e:
        return str(e)
    


@app.route("/extPdf")
def extPdf():
    filename = session.get('filenames', '')
    result = collection.find_one({"filename": filename[-1]})
    # print(result['data'])
    pdf_stream = io.BytesIO(result['data'])
    pdf_content = pdf_stream.getvalue()
    # pdf_document = fitz.open(pdf_stream)
    text=textPdf.extTEXT(pdf_content)
    lang=All.langDetect(text)
    return render_template("pdfext.html",given=text,language=lang)






if __name__ == "__main__":
	app.run(debug=True)
