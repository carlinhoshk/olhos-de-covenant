import numpy as np
import cv2 as cv
import time


desenhoBranco = np.zeros((512, 512,3), np.uint8)
font = cv.FONT_HERSHEY_TRIPLEX
font1 = cv.FONT_HERSHEY_DUPLEX
t = time.localtime()
horario = time.strftime("%H:%M:%S", t)
contador = 0 
#---------QuadradoBranco-------------------------

#cv.rectangle(desenhoBranco, (500, 0), (0,500), (255, 255, 255), 2)
contador+=1
cv.rectangle(desenhoBranco, (512, 0), (0,50), (0, 255, 0), -1)
cv.putText(desenhoBranco, f'ID{contador}', (200, 45), font1, 1.0, (255, 255,255),1)
cv.putText(desenhoBranco, f'{horario}', (200, 90), font, 1.0, (255, 255, 255), 1)


#cv.line(desenhoBranco,(0,0), (511, 511), (255,0,0),5)

cv.imshow('Tela Branca', desenhoBranco)
cv.waitKey(0)


