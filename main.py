from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

im = Image.open('image.png')

print(pytesseract.image_to_string(im, lang = 'eng'))

# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('image.png', extension = 'pdf')
with open('text.pdf', 'w+b') as f:
    f.write(pdf)
    