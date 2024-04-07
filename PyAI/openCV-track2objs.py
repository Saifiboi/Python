import cv2
import numpy as np
print(cv2.__version__)
def mycall1(val):
    global hueLow1
    print('Hue Low 1:',val)
    hueLow1=val
def mycall2(val):
    global hueHigh1
    print('Hue High 1:',val)
    hueHigh1=val
def mycall3(val):
    global hueLow2
    print('Hue Low 2:',val)
    hueLow2=val
def mycall4(val):
    global hueHigh2
    print('Hue High 2:',val)
    hueHigh2=val
def mycall5(val):
    global satLow
    print('Sat Low:',val)
    satLow=val
def mycall6(val):
    global satHigh
    print('Sat High:',val)
    satHigh=val
def mycall7(val):
    global valLow
    print('Val Low:',val)
    valLow=val
def mycall8(val):
    global valHigh
    print('Val High:',val)
    valHigh=val
hueLow1=10
hueHigh1=20
hueLow2=10
hueHigh2=20
satLow=10
satHigh=250
valLow=10
valHigh=250
width=320
height=180
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 15)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
cv2.namedWindow('my Trackbars')
cv2.resizeWindow('my Trackbars',640,450)
cv2.createTrackbar('hue Low 1','my Trackbars',10,179,mycall1)
cv2.createTrackbar('hue High 1','my Trackbars',20,179,mycall2)
cv2.createTrackbar('hue Low 2','my Trackbars',10,179,mycall3)
cv2.createTrackbar('hue High 2','my Trackbars',20,179,mycall4)
cv2.createTrackbar('sat Low','my Trackbars',10,255,mycall5)
cv2.createTrackbar('sat High','my Trackbars',250,255,mycall6)
cv2.createTrackbar('val Low','my Trackbars',10,255,mycall7)
cv2.createTrackbar('val High','my Trackbars',250,255,mycall8)
cv2.namedWindow('my WEBcam')
cv2.resizeWindow('my WEBcam',width,height)
while True:
    ignore, frame = cam.read()
    frame = cv2.flip(frame, 1)
    frameHSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_bound1=np.array([hueLow1,satLow,valLow])
    lower_bound2=np.array([hueLow2,satLow,valLow])
    upper_bound1=np.array([hueHigh1,satHigh,valHigh])
    upper_bound2=np.array([hueHigh2,satHigh,valHigh])
    mymask1=cv2.inRange(frameHSV,lower_bound1,upper_bound1)
    mymask2=cv2.inRange(frameHSV,lower_bound2,upper_bound2)
    mymask1=cv2.bitwise_and(frame,frame,mask=mymask1)
    mymask2=cv2.bitwise_and(frame,frame,mask=mymask2)
    mymask=cv2.bitwise_or(mymask1,mymask2)
    cv2.imshow('my Mask',mymask)
    cv2.moveWindow('my Mask',0,height)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    cv2.moveWindow('my Trackbars',width,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()