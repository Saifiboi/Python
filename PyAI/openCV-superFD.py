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
mpDraw=mp.solutions.drawing_utils
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    facesData=DataConverter.MPSimplifiedData.captureFacedata(frameRGB,width,height)
    if len(facesData) !=0:
        for face in facesData:
            cv2.rectangle(frame,face['topLeft'],face['bottomRight'],(255,0,0),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()