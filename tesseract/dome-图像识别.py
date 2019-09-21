#encoding:utf-8

from PIL import Image
from pytesseract import pytesseract

pytesseract.pytesseract.tesseract_cmd= r"C:\OCR\Tesseract-OCR\tesseract.exe"

# for i in range(3):
image = Image.open('a123.png')

text = pytesseract.image_to_string(image, lang='chi_sim')

print(text)

