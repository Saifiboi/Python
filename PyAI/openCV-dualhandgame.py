import cv2
import mediapipe as mp
import DataConverter
print(cv2.__version__)
width=640
height=360
font=cv2.FONT_HERSHEY_SIMPLEX
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
mpDraw=mp.solutions.drawing_utils
paddlewidth=25
paddleheight=125
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
        cv2.putText(frame,'Game Over!',(int(width/2),int(height/2)),font,0.5,(0,255,0),2)
        cv2.imshow('my WEBcam', frame)
        cv2.moveWindow('my WEBcam',0,0)
        cv2.waitKey(10000)
        break
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    MLM_list,handsType=DataConverter.MPSimplifiedData.captureHanddata(frameRGB,width,height)
    if len(MLM_list) !=0:
        for hand,handType in zip(MLM_list,handsType):
            cv2.circle(frame,(circle_x_axis,circle_y_axis),10,(0,0,255),-1)
            if handType=="Left":
                cv2.rectangle(frame,(0,int(hand[8][1]-paddleheight/2)),(paddlewidth,int(hand[8][1]+paddleheight/2)),paddleColor,-1)
                if (circle_y_axis >= int(hand[8][1]-paddleheight/2) and circle_y_axis <=int(hand[8][1]+paddleheight/2)) and (circle_x_axis <= paddlewidth):
                    width_inc=width_inc *-1
            if handType=="Right":
                cv2.rectangle(frame,(width-paddlewidth,int(hand[8][1]-paddleheight/2)),(width,int(hand[8][1]+paddleheight/2)),paddleColor,-1)      
                if (circle_y_axis >= int(hand[8][1]-paddleheight/2) and circle_y_axis <=int(hand[8][1]+paddleheight/2)) and (circle_x_axis >= width-paddlewidth):
                    width_inc=width_inc* -1
        if circle_x_axis<=0 or circle_x_axis >=width:
            lives =lives -1
            circle_x_axis=int(width/2)
            circle_y_axis=int(height/2)
            height_inc=5
            width_inc=5
        if circle_y_axis <= 0 or circle_y_axis>= height:
            height_inc=height_inc* -1
        circle_x_axis=circle_x_axis+width_inc
        circle_y_axis=circle_y_axis+height_inc
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()