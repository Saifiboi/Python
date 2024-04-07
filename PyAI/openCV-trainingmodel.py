import os
import cv2
import numpy as np
import face_recognition as FR
font=cv2.FONT_HERSHEY_SIMPLEX
fileLoc='C:\\Users\Safi\Documents\Python\PyAI\demoImages\known'
names=[]
knownEncodings=[]
for root,dirs,files in os.walk(fileLoc):
    for file in files:
        filepath=os.path.join(root,file)
        personFace=FR.load_image_file(filepath)
        personEncoding=FR.face_encodings(personFace)[0]
        knownEncodings.append(personEncoding)
        names.append(os.path.splitext(file)[0])
np.savez('encodings',encodings=knownEncodings,names=names)
