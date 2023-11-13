import pypdfium2 as pdfium
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
from pytesseract import image_to_string 

class textPdf:
    def __init__(self) -> None:
        pass
    def convert_pdf_to_images(file_path, scale=300/72):
        
        pdf_file = pdfium.PdfDocument(file_path)  
        page_indices = [i for i in range(len(pdf_file))]
        
        renderer = pdf_file.render(
            pdfium.PdfBitmap.to_pil,
            page_indices = page_indices, 
            scale = scale,
        )
        
        list_final_images = [] 
        
        for i, image in zip(page_indices, renderer):
            
            image_byte_array = BytesIO()
            image.save(image_byte_array, format='jpeg', optimize=True)
            image_byte_array = image_byte_array.getvalue()
            list_final_images.append(dict({i:image_byte_array}))
        
        return list_final_images


    # def display_images(list_dict_final_images):
        
    #     all_images = [list(data.values())[0] for data in list_dict_final_images]

    #     for index, image_bytes in enumerate(all_images):

    #         image = Image.open(BytesIO(image_bytes))
    #         figure = plt.figure(figsize = (image.width / 100, image.height / 100))

    #         plt.title(f"----- Page Number {index+1} -----")
    #         plt.imshow(image)
    #         plt.axis("off")
    #         plt.show()





    def extract_text_with_pytesseract(list_dict_final_images):
        
        image_list = [list(data.values())[0] for data in list_dict_final_images]
        image_content = []
        
        for index, image_bytes in enumerate(image_list):
            
            image = Image.open(BytesIO(image_bytes))
            raw_text = str(image_to_string(image))
            image_content.append(raw_text)
        
        return "\n".join(image_content)


    def extTEXT(pdfF):
        convert_pdf_to_images = textPdf.convert_pdf_to_images(pdfF)
        # textPdf.display_images(convert_pdf_to_images)
        text_with_pytesseract = textPdf.extract_text_with_pytesseract(convert_pdf_to_images)
            # print(text_with_pytesseract)
        return text_with_pytesseract 
        