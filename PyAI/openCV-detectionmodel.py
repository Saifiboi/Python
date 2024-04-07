import os
import cv2
import numpy as np
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
npzfile = np.load('encodings.npz')
knownEncodings=npzfile['encodings']
names=npzfile['names']
unknownFace=FR.load_image_file('C:/Users/Safi/Documents/Python/PyAI/demoImages/unknown/u2.jpg')
unknownFaceBGR=cv2.cvtColor(unknownFace,cv2.COLOR_RGB2BGR)
unkonownFaceLocations=FR.face_locations(unknownFace)
unknownFaceEncodings=FR.face_encodings(unknownFace)
name='unknown'
for location,Encoding in zip(unkonownFaceLocations,unknownFaceEncodings):
    top,left,bottom,right=location
    cv2.rectangle(unknownFaceBGR,(left,top),(right,bottom),(255,0,0),3)
    matches=FR.compare_faces(knownEncodings,Encoding)
    if True in matches:
        matchIndex=matches.index(True)
        name=names[matchIndex]
    cv2.putText(unknownFaceBGR,name,(left,top),font,0.75,(0,0,255),3)
cv2.imshow('My Window',unknownFaceBGR)
cv2.waitKey(10000)