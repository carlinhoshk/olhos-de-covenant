import cv2 as cv, numpy as np                # 18/07/2022-22:22 padronizar a utlização de "as" para bibliotecas cv2 para cv

########################Parametros e Variaveis#############################

camera = cv.VideoCapture("rtsp://admin:SenhaGenerica223@192.168.15.28")



########################Leitura Camera#####################################

while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break
    frame = cv.resize(frame, (700,700))
    cv.imshow("Mostrando Camera Frente Casa....", frame)
    print(frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv.destroyAllWindows()



