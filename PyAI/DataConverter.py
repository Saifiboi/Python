import cv2
import mediapipe as mp
class MPSimplifiedData:
    def captureHanddata(frameRGB,width,height):
        hands=mp.solutions.hands.Hands(False,1)
        results=hands.process(frameRGB)
        MLM_list=[]
        handsType=[]
        if results.multi_hand_landmarks is not None:
            for hand in results.multi_handedness:
               handsType.append(hand.classification[0].label) 
            for handLandmarks in results.multi_hand_landmarks:
                hLM_list=[]
                for singleLandmark in handLandmarks.landmark:
                    hLM_list.append((int(singleLandmark.x*width),int(singleLandmark.y*height)))
                MLM_list.append(hLM_list)
            return MLM_list,handsType
        else :
            return [],[]
    def capturePosedata(frameRGB,width,height):
        pose=mp.solutions.pose.Pose(False,False,True)
        results=pose.process(frameRGB)
        pose_landmarks=[]
        if results.pose_landmarks !=None:
            for lm in results.pose_landmarks.landmark:
                pose_landmarks.append((int(lm.x*width),int(lm.y*height)))
        return pose_landmarks
    
    def captureFacedata(frameRGB,width,height):
        findface=mp.solutions.face_detection.FaceDetection()
        results=findface.process(frameRGB)
        facesData=[]
        if results.detections != None:
            for face in results.detections:
                bbox=face.location_data.relative_bounding_box
                topleft=(int(bbox.xmin*width),int(bbox.ymin*height))
                bottomright=(int((bbox.xmin+bbox.width) * width),int((bbox.ymin+bbox.height) * height))
                facesData.append({'topLeft':topleft,'bottomRight':bottomright})
        return facesData

class MPFaceParsing:
    def faceDrawset(frame,circle_thickness=3,circle_radius=2,circle_color=(255,0,0),line_thickness=0,line_color=(0,0,255)):
        frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        faceMesh=mp.solutions.face_mesh.FaceMesh(False,3)
        results=faceMesh.process(frameRGB)
        mpDraw=mp.solutions.drawing_utils
        drawspecline=mpDraw.DrawingSpec(thickness=line_thickness,circle_radius=circle_radius,color=line_color)
        drawspeccircle=mpDraw.DrawingSpec(thickness=circle_thickness,circle_radius=circle_radius,color=circle_color)
        for faceLandmarks in results.multi_face_landmarks:
            mpDraw.draw_landmarks(frame,faceLandmarks,mp.solutions.face_mesh.FACEMESH_TESSELATION,drawspeccircle,drawspecline)
        return frame
    def captureFaceMesh(frameRGB,width,height):
        faceMesh=mp.solutions.face_mesh.FaceMesh(False,3)
        results=faceMesh.process(frameRGB)
        mesh=[]
        if results.multi_face_landmarks !=None:
            for faceLandmarks in results.multi_face_landmarks:
                for lm in faceLandmarks.landmark:
                    mesh.append((int(lm.x*width),int(lm.y*height)))
        return mesh
                    
                    
                