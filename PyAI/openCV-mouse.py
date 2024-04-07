import cv2
import time
print(cv2.__version__)
evnt = 0
pnt = (0, 0)
pnt2 = (0, 0)
def ClickMouse(event, xpos, ypos, flag, params):
    global evnt,pnt,pnt2
    if event==cv2.EVENT_LBUTTONDOWN:
        pnt=(xpos, ypos)
        print(f"event 1 occured at :{pnt}") 
    if event==cv2.EVENT_LBUTTONUP:
        pnt2=(xpos, ypos)
        print(f"event 2 occured at :{pnt2}") 
    evnt=event
        
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
initial_place_hor = 0
initial_place_ver = 0
step_hor = 60
step_ver =  80
add_hor = 1
add_ver = 1
cv2.namedWindow('my WEBcam')
cv2.setMouseCallback('my WEBcam',ClickMouse)
check = False
while True:
    ignore, fram = cam.read()
    frame = cv2.flip(fram, 1)
    if  not ignore:
        print("frame not read")
        exit(1)
    curr_time = time.time()
    FPS = 1 / (curr_time - prev_time)
    fpsFilt = fpsFilt * 0.74 + FPS * 0.25
    if evnt==4 or check:
        cv2.rectangle(frame,pnt,pnt2,(0,0,255),2)
        if pnt[0] < pnt2[0]:
            start_pos_y = (pnt[0], pnt2[0])
        elif pnt[0] > pnt2[0]:
            start_pos_y = (pnt2[0], pnt[0])
        if pnt[1] < pnt2[1]:
            start_pos_x = (pnt[1], pnt2[1])
        elif pnt[1] > pnt2[1]:
            start_pos_x = (pnt2[1], pnt[1])
        ROI = frame[start_pos_x[0]:start_pos_x[1], start_pos_y[0]:start_pos_y[1]] 
        if len(ROI) != 0:
            cv2.imshow('my ROI', ROI)
            cv2.moveWindow('my ROI', 650, 0)
            check = True
    if evnt==5:
        check = False
        cv2.destroyWindow('my ROI') 
        evnt = 0
    prev_time = time.time()
    text = f"FPS:{int(fpsFilt)}"
    counter = 1
    cv2.putText(frame, text=text, org=(60, 40), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255), thickness=1)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam', 0, 0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    counter += 1