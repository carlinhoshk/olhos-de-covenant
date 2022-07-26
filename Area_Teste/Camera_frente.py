import cv2 as cv, numpy as np  
import face_recognition
import time
             # 18/07/2022-22:22 padronizar a utlização de "as" para bibliotecas cv2 para cv

########################Parametros e Variaveis#############################

camera = cv.VideoCapture("ibmface.mp4")

contador = 0

#camera = cv.VideoCapture("rtsp://admin:SenhaGenerica223@192.168.15.28")

font = cv.FONT_HERSHEY_DUPLEX

########################Leitura Camera#####################################

while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break
    #frame = cv.resize(frame, (700,700))
    contador+=1
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)

    for (top, right, bottom, left) in (face_locations):
        top *=4
        right *=4
        bottom *=4
        left *=4

        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        cv.putText(frame, f'{contador}', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)




    cv.imshow("Mostrando Camera Frente Casa....", frame)
    print(frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv.destroyAllWindows()



