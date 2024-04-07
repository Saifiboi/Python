import cv2
import numpy as np
import DataConverter
import pickle
print(cv2.__version__)
def distance(pt1,pt2):
    return ((pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2)**(1.0/2)
def findDistances(handData):
    distMatrix=np.zeros([len(handData),len(handData)],dtype='float')
    for row in range(0,len(handData)):
        for column in range(0,len(handData)):
            distMatrix[row][column]=distance(handData[row],handData[column])/distance(handData[0],handData[9])
    return distMatrix

def findError(gestureMatrix,unknownMatrix,keyPoints):
    error=0
    for row in keyPoints:
        for column in keyPoints:
            error=error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
    return error
def findGesture(unknownGesture,knownGestures,Keypoints,names,tol):
    errors=[]
    for gesture in knownGestures:
        errors.append(findError(gesture,unknownGesture,Keypoints))
    gestureIndex=0
    for i in range(1,len(knownGestures)):
        if errors[i] < errors[gestureIndex]:
            gestureIndex=i
    if errors[gestureIndex] <= tol:
        return names[gestureIndex]
    else :
        return 'unknown'
        
width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
keyPoints=[0,4,5,9,13,17,8,12,16,20]
train=int(input('Enter 1 for training 0 for loading :'))
if train==1:
    noGestures=int(input('Enter Number of Gestures you wanna train upon: '))
    gesturesName=[]
    for i in range(0,noGestures):
        gesturesName.append(input(f'Enter name of Gesture # {i+1} : '))
    curr_index=0
    knownGestures=[]
    file=input('Which File do you wanna write into(Press Enter for default) : ')
    if file=='':
        file='default'
    file = file + '.pk1'
if train==0:
    file=input('Which File do you wanna load from(Press Enter for default) : ')
    if file=='':
        file='default'
    file = file + '.pk1'
    with open(file,'rb') as f:
        gesturesName=pickle.load(f)
        knownGestures=pickle.load(f)
tol=10
while True:
    ignore,  frame = cam.read()
    frame=cv2.flip(frame,1)
    frame=cv2.resize(frame,(width,height))
    frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    handData,exept=DataConverter.MPSimplifiedData.captureHanddata(frameRGB,width,height)
    if train==1:
        if len(handData) != 0:
            print(f'Show Your {gesturesName[curr_index]} Gesture,press t when Ready')
            if cv2.waitKey(1) & 0xff==ord('t'):
                knownGesture=findDistances(handData[0])
                knownGestures.append(knownGesture)
                curr_index=curr_index+1
                if curr_index==noGestures:
                    train=0
                    with open(file,'wb') as f:
                        pickle.dump(gesturesName,f)
                        pickle.dump(knownGestures,f)
    if train==0:
        if len(handData) !=0:
            unknownGesture=findDistances(handData[0])
            gestureName=findGesture(unknownGesture,knownGestures,keyPoints,gesturesName,tol)
            cv2.putText(frame,gestureName,(100,100),1,1,(255,0,0),3)
    for hand in handData:
                for ind in keyPoints:
                    cv2.circle(frame,hand[ind],10,(255,0,255),3)
    cv2.imshow('my WEBcam', frame)
    cv2.moveWindow('my WEBcam',0,0)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break
cam.release()