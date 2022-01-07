import pytesseract
import pandas as pd
from PIL import Image
from IPython.display import display
import easyocr

imagem = (Image.open("Imagem.jpeg"))

reader = easyocr.Reader(lang_list= ["pt"])

output = reader.readtext(imagem, detail=0)

print(output)


#texto = pytesseract.image_to_string(Image.open(imagem))

#print(texto)
