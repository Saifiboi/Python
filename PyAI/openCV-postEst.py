import cv2
import DataConverter
import mediapipe as mp
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
pose=mp.solutions.pose.Pose(False,False,True)
mpDraw=mp.solutions.drawing_utils
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    pose_landmarks=DataConverter.MPSimplifiedData.capturePosedata(frameRGB,width,height)
    if len(pose_landmarks)!=0:
        cv2.circle(frame,pose_landmarks[0],5,(255,0,0),2)
        cv2.circle(frame,pose_landmarks[2],5,(0,0,255),2)
        cv2.circle(frame,pose_landmarks[5],5,(0,0,255),2)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()