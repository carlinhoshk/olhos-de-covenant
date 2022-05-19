import os, cv2, mahotas, time
import easyocr
from PIL import Image
###############################################################################

reader = easyocr.Reader(['pt','pt'])
def edicão_placa(img2):
    img = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    imgcorte_alt_alt = int(img.shape[0] * 0.33)
    imgcorte_alt_baix = int(img.shape[0] * 0.87)
    imgcorte_lad_dir = int(img.shape[1] * 0.07)
    imgcorte_lad_esq = int(img.shape[1] * 0.97)
    recorte = img[imgcorte_alt_alt:imgcorte_alt_baix, imgcorte_lad_dir:imgcorte_lad_esq]
    cv2.imshow("recorte", recorte)
    suave = cv2.GaussianBlur(recorte, (3, 3), 10)
    T = mahotas.thresholding.otsu(suave)
    temp = recorte.copy()
    temp[temp > T] = 255
    temp[temp < 255] = 0
    temp = cv2.bitwise_not(temp)
    blur_mediana = cv2.medianBlur(temp, 13)
    blur = cv2.blur(blur_mediana, (9, 21))
    cv2.imwrite("Placa filtrada.jpg", blur)
    return blur
###############################################################################
blur = 0
camera = cv2.VideoCapture(0)
df = cv2.CascadeClassifier('placas_original.xml')
placa_escrita = 0
while True:
    (sucesso, frame) = camera.read()
imgPB = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
placas = df.detectMultiScale(imgPB, scaleFactor=1.02, minNeighbors=10,
minSize=(60,60),flags=cv2.CASCADE_SCALE_IMAGE)
imgPB_temp = imgPB.copy()
imgC = frame
cv2.imshow("Encontrando placas...", frame)
if (b == 0):
    for (x, y, w, h) in placas:
        a = a +1
        placa = frame[y:y + h, x:x + w]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        cv2.imwrite("imagem_frame.jpg", frame)
        edicão_placa(placa)
        caracs = blur
        caracs = reader.readtext(Image.open("Placa filtrada.jpg", detail = 0),lang="amh")
        caracs = caracs.replace(' ', '')
        caracs = caracs.replace("-", "")
        letras = caracs[:3]
        num = caracs[3:]
        num = num.replace("-", "")
        letras = letras.replace("-", "")
        num = num.replace('O', "0")
        letras = letras.replace('0', "O")
        num = num.replace('I', "1")
        letras = letras.replace('1', "I")
        num = num.replace('G', "6")
        letras = letras.replace('6', "G")
        num = num.replace('B', "8")
        letras = letras.replace('8', "B")
        num = num.replace('T', "1")
        letras = letras.replace('1', "T")
        num = num.replace('Z', "2")
        letras = letras.replace('2', "Z")
        num = num.replace('H', "11")
        letras = letras.replace('11', "H")
        num = num.replace('S', "5")
        letras = letras.replace('5', "S")
        placa_escrita = letras + '-' + num
        print(placa_escrita[:8])
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break
camera.release()
cv2.destroyAllWindows()
