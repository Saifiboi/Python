import cv2
import time
x_value = 0
y_value = 0
print(cv2.__version__)
def MoveTracebar1(val):
    global x_value
    print(val)
    x_value = val   
def MoveTracebar2(val):
    global y_value 
    print(val)
    y_value = val   
def MoveTracebar3(val):
    global height,width 
    print(val)
    height = val
    width = int(9/16*val)   
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FPS, 15)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
prev_time = time.time()
time.sleep(0.1)
cv2.namedWindow('my Tracebars')
cv2.resizeWindow('my Tracebars', 400, 150)
cv2.createTrackbar('move window_x', 'my Tracebars',0,650,MoveTracebar1)
cv2.moveWindow('my Tracebars', width, 0)
cv2.createTrackbar('move window_y', 'my Tracebars',0,280,MoveTracebar2)
cv2.moveWindow('my Tracebars', width, 0)
cv2.createTrackbar('resize', 'my Tracebars',height,1280,MoveTracebar3)
cv2.moveWindow('my Tracebars', width, 0)
fpsFilt = 15
while True:
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
    ignore,  fram = cam.read()
    frame = cv2.flip(fram, 1)
    curr_time = time.time()
    FPS = 1/(curr_time-prev_time)
    fpsFilt = fpsFilt*0.74 + FPS*0.25
    prev_time = time.time()
    text = f"FPS:{int(fpsFilt)}"
    counter = 1
    cv2.putText(frame, text=text,org=(60,40), fontFace=cv2.FONT_HERSHEY_DUPLEX ,fontScale= 1,color=(0,0,255), thickness=1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',x_value,y_value)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
    counter += 1
cam.release()