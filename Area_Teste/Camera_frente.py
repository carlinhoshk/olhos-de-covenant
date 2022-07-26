import cv2 as cv, numpy as np  
import face_recognition
import time
import asyncio
             # 18/07/2022-22:22 padronizar a utlização de "as" para bibliotecas cv2 para cv

#----função corta foto-----

def corta_foto(x):

    cv.imshow("cortada", x)
    print(x)
    time.sleep(10)
    
    

########################Parametros e Variaveis#############################

camera = cv.VideoCapture("wenca.mp4")

contador = 0
t = time.localtime()
horario = time.strftime("%H:%M:%S", t)
#camera = cv.VideoCapture("rtsp://admin:SenhaGenerica223@192.168.15.28")
frame_num = 0
font = cv.FONT_HERSHEY_DUPLEX
font1 = cv.FONT_HERSHEY_DUPLEX

########################Leitura Camera#####################################

while True:

    (sucesso, frame) = camera.read()
    if not sucesso:
        break
    #frame = cv.resize(frame, (700,700))
    frame_num += 1
    small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_small_frame)

    for (top, right, bottom, left) in (face_locations):
        top *=4
        right *=4
        bottom *=4
        left *=4


        contador+=1
        cv.rectangle(frame, (512, 0), (0,50), (0, 255, 0), -1)
        cv.rectangle(frame, (512, 50), (0,100), (0, 0, 0), -1)
        cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv.putText(frame, f'Contador de pessoa {contador}', (100, 30), font1, 1.0, (255, 255,255),1)
        cv.putText(frame, f'{horario}', (200, 90), font, 1.0, (255, 255, 255), 1)
        #cv.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #cv.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv.FILLED)
        #cv.putText(frame, f'{contador}', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
 
        #face_cortada = frame[y:right+left, 
        x=0
        y=0
        #face_cortada = cv.getRectSubPix(frame, (y-100, x+30), (right, left))
        crop_rate = 30
        #time.sleep(30)
        face_cortada = frame[x:right+left, y:top+left+200]


        #cv.imshow("cortada", face_cortada)
        if frame_num % crop_rate == 0:
            corta_foto(face_cortada)
        cv.imwrite(f'dados/id{contador}.jpg', face_cortada)



    cv.imshow("Mostrando Camera Frente Casa....", frame)
    #print(frame)
    if cv.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv.destroyAllWindows()



