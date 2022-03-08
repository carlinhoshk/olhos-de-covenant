import easyocr
import cv2
import os
import numpy as np

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
# point to license plate image (works well with custom crop function)
reader = easyocr.Reader(['pt','pt'])
gray = cv2.imread("placa.png", 0)
#gray = cv2.resize( gray, None, fx = 3, fy = 3, interpolation = cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(gray, (5,5), 0)
gray = cv2.medianBlur(gray, 3)
# perform otsu thresh (using binary inverse since opencv contours work better with white text)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)
rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))

# apply dilation 
dilation = cv2.dilate(thresh, rect_kern, iterations = 1)
cv2.imshow("dilation", dilation)
leitura0 = str(reader.readtext(dilation, detail = 0))

num = leitura0[2:]
numero = num.replace(",", "")
print(numero)
cv2.waitKey(0)