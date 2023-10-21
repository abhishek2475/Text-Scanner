from flask import Flask, render_template, request
#from main import *

app = Flask(__name__)


@app.route("/")
def index():
	s = 1
	return render_template("index.html",given=s)
@app.route("/dilate",methods=['POST'])
def upload_image():
    if 'image' in request.files:
        image = request.files['image']
        # You can now process the 'image' object, e.g., save it or perform any necessary operations.
        # Example: Save the image to a specific directory
        image.save('uploads/' + image.filename)
        return 'Image uploaded successfully!'
    return 'No image uploaded.'

if __name__ == "__main__":
	app.run(debug=True)
