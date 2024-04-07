import cv2
import face_recognition as fr
font=cv2.FONT_HERSHEY_SIMPLEX
saifFace=fr.load_image_file('C:/Users/Safi/Documents/Python/PyAI/demoImages/known/saif.jpg')
saiffaceLoc=fr.face_locations(saifFace)[0]
saiffaceEncode=fr.face_encodings(saifFace)[0]
knownfaceEncodings=[saiffaceEncode]
names=['Saif']
width=640
height=320
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    faceLocations=fr.face_locations(frameRGB)
    unknownFaceEncodings=fr.face_encodings(frameRGB)
    for face_Location,face_Encoding in zip(faceLocations,unknownFaceEncodings):
        top,right,bottom,left=face_Location
        cv2.rectangle(frame,(left,top),(right,bottom),(0,0,255),3)
        name='unknown'
        matches=fr.compare_faces(knownfaceEncodings,face_Encoding)
        print(matches)
        if True in matches:
            matchIndex=matches.index(True)
            name=names[matchIndex]
        cv2.putText(frame,name,(left,top),font,0.75,(255,0,0),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()
