from pytesseract import image_to_string 
from PIL import Image
text =  image_to_string(Image.open('plate.jpg'))

with open('test.txt', mode = 'w') as f:
    f.write(text)
