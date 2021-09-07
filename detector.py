import cv2 
import numpy as np 
import pickle
import sqlite3

rec = cv2.face.LBPHFaceRecognizer_create()
faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
rec.read("recognizer/trainning.yml")
path = "dataSet"


def getProfile(id):
    conn = sqlite3.connect('FaceBase.db')
    cmd = "select * from people where id =" + str(id)
    cursor = conn.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    conn.close()
    return profile


cam = cv2.VideoCapture(0) 
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cam.read()
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(
        gray, 
        scaleFactor=1.2, 
        minNeighbors=5, 
        minSize=(100, 100), 
        flags= cv2.CASCADE_SCALE_IMAGE)

    for(x, y, w, h) in faces:
        nbr_prodicted, conf = rec.predict(gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
        profile = getProfile(nbr_prodicted)

        if(profile != None):
            cv2.putText(img,"Name: "+str(profile[1]),(x,y+h + 30),font,1,(255,0,0),2)
            cv2.putText(img,"Age: "+str(profile[2]),(x,y+h + 60),font,1,(255,0,0),2)

    cv2.imshow("Face", img)
    if(cv2.waitKey(1) == ord('q')):
        break

cam.release()
cv2.destroyAllWindows()