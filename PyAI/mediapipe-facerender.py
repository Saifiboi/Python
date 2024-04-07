import cv2
import mediapipe as mp
import DataConverter
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    # frame=DataConverter.MPFaceParsing.faceDrawset(frame)
    facemesh=DataConverter.MPFaceParsing.captureFaceMesh(frameRGB,width,height)
    for mesh in facemesh:
        cv2.circle(frame,mesh,1,(0,255,255),-1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()