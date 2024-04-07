import cv2
import time
print(cv2.__version__)
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 15)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
prev_time = time.time()
time.sleep(0.1)
fpsFilt = 15
while True:
    ignore,  frame = cam.read()
    curr_time = time.time()
    FPS = 1/(curr_time-prev_time)
    fpsFilt = fpsFilt*0.74 + FPS*0.25
    prev_time = time.time()
    text = f"FPS:{int(fpsFilt)}"
    counter = 1
    cv2.putText(frame, text=text,org=(60,40), fontFace=cv2.FONT_HERSHEY_DUPLEX ,fontScale= 1,color=(0,0,255), thickness=1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
    counter += 1
cam.release()