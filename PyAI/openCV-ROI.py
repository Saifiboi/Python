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
initial_place_hor = 0
initial_place_ver = 0
step_hor = 60
step_ver =  80
add_hor = 1
add_ver = 1
while True:
    if step_hor == height or (initial_place_hor == 0 and add_hor < 0):
        add_hor *= -1
    if step_ver == width or (initial_place_ver == 0 and add_ver < 0):
        add_ver *= -1
    ignore, frame = cam.read()
    frame_grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_grey_bgr = cv2.cvtColor(frame_grey, cv2.COLOR_GRAY2BGR)
    moving_frame = frame[initial_place_hor : step_hor, initial_place_ver : step_ver]
    frame_grey_bgr[initial_place_hor : step_hor, initial_place_ver : step_ver] = moving_frame

    curr_time = time.time()
    FPS = 1 / (curr_time - prev_time)
    fpsFilt = fpsFilt * 0.74 + FPS * 0.25
    prev_time = time.time()
    text = f"FPS:{int(fpsFilt)}"
    counter = 1
    cv2.putText(frame_grey_bgr, text=text, org=(60, 40), fontFace=cv2.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 0, 255), thickness=1)
    cv2.imshow('my move', moving_frame)
    cv2.moveWindow('my move', 650, 0)
    cv2.imshow('my WEBcam', frame_grey_bgr)
    cv2.moveWindow('my WEBcam', 0, 0)
    initial_place_hor += add_hor
    initial_place_ver += add_ver
    step_hor += add_hor
    step_ver += add_ver

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    counter += 1
cv2.camrelease()
