import numpy as np
import cv2

frame = np.zeros([256, 720, 3], dtype="uint8")
frame2 = np.zeros([256, 720, 3], dtype="uint8")
for row in range(0, 256):
    for column in range(0, 720):
        frame[row,column] = (int(column/4), row, 255)
        frame2[row,column] = (int(column/4), 255, row)
frame=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
frame2=cv2.cvtColor(frame2,cv2.COLOR_HSV2BGR)
while True:
    cv2.imshow('my rainbow', frame)
    cv2.imshow('val rainbow', frame2)
    cv2.moveWindow('my rainbow', 0, 0)
    cv2.moveWindow('val rainbow',0 , 256)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllwindows()
        
