from PIL import Image
import pytesseract

from googletrans import Translator

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

class TraductorImagenes:

    def __init__(self, image):
        self.image = image
    def translate(self):
        # text = pytesseract.image_to_string(Image.open('test.png'))
        text = pytesseract.image_to_string(self.image)
        if text:
            print("TEXTO RECOGIDO DE LA IMAGEN")
            print("-"*50)
            print(text)
            print("-"*50)
            trasnlator = Translator()

            trasnlated_text = trasnlator.translate(text, src='en',dest='es').text
            print("TEXTO RTRADUCIDO")
            print("-"*50)
            print(trasnlated_text)
            print("-"*50)
        else:
            print('Error')