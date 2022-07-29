import cv2 as cv
import numpy as np
import time
import face_recognition


video_capture = cv.VideoCapture("rtsp://admin:SenhaGenerica223@192.168.15.28")
#video_capture.open()

#---Variveis------------------------

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

#----------------------------------

while True:

    ret, frame = video_capture.read()

    if process_this_frame:

        small_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        #face_encodings = face_recognition.face.encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left) in (face_locations):

            top *=4
            right *=4
            bottom *=4
            left *=4

            cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0),2)

            cv.rectangle(frame, (left,bottom -35), (right, bottom), (0,0,255), cv.FILLED)

            cv.imshow('video', frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break
video_capture.release()
cv2.destroyAllWindows()