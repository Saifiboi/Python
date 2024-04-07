import cv2
import mediapipe as mp
import HandData
print(cv2.__version__)
width=640
height=360
font=cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
hands=mp.solutions.hands.Hands(False,2)
mpDraw=mp.solutions.drawing_utils
paddlewidth=125
paddleheight=25
paddleColor=(0,255,0)
lives=5
circle_x_axis=int(width/2)
circle_y_axis=int(height/2)
height_inc=5
width_inc=5
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    if lives == 0:
        cv2.putText(frame,'Game Over!',(int(width/2),int(height/2)),font,0.5,(0,255,0),15)
        cv2.imshow('my WEBcam', frame)
        cv2.moveWindow('my WEBcam',0,0)
        cv2.waitKey(10000)
        break
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results=hands.process(frameRGB)
    MLM_list=HandData.handdata.capture2Ddata(results,width,height)
    if len(MLM_list) !=0:
        for hand in MLM_list:
            cv2.circle(frame,(circle_x_axis,circle_y_axis),10,(0,0,255),-1)
            cv2.rectangle(frame,(int(hand[8][0]-paddlewidth/2),0),(int(hand[8][0]+paddlewidth/2),paddleheight),paddleColor,-1)
            cv2.rectangle(frame,(int(hand[8][0]-paddlewidth/2),height-paddleheight),(int(hand[8][0]+paddlewidth/2),height),paddleColor,-1)
            if (circle_x_axis >=int(hand[8][0]-paddlewidth/2)  and circle_x_axis <= int(hand[8][0]+paddlewidth/2)) and (circle_y_axis<=paddleheight or circle_y_axis>= height-paddleheight):
                height_inc=height_inc * -1
            elif circle_y_axis+height_inc >= height or circle_y_axis+height_inc <= 0:
                lives=lives -1
                circle_x_axis=int(width/2)
                circle_y_axis=int(height/2)
                height_inc=5
                width_inc=5
            if (circle_x_axis >= width or circle_x_axis <= 0) :
                width_inc=width_inc * -1
        circle_x_axis=circle_x_axis+width_inc
        circle_y_axis=circle_y_axis+height_inc
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()