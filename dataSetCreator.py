import cv2
import sqlite3
import os.path
import numpy as np
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(_file_))
db_path = os.path.join(BASE_DIR, "FaceBase.db")


faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


def insertOrUpdate(Id, Name, Age):
    conn = sqlite3.connect(db_path)
    cmd = "select * from people where id =" + str(Id)
    cursor = conn.execute(cmd)
    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 1):
        cmd = "update people set name=" + str(Name) + "set age=" +str(age) + "where id =" + str(id)
    else:
        cmd = "insert into people(id, name, age) VALUES(?,?,?)"
        datos = (str(Id),str(Name),str(Age))

    conn.execute(cmd, datos)
    conn.commit()
    conn.close()


id = input("Ingresa tu id: ")
name = input("Ingresa tu nombre: ")
age = input("Ingresa tu edad: ")

insertOrUpdate(id, name, age)


sampleNum = 0
while True:
    ret , img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)

    for(x, y, w, h) in faces:
        sampleNum = sampleNum + 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)
        cv2.waitKey(100)

    cv2.imshow("Face", img)
    cv2.waitKey(1)
    if(sampleNum > 20):
        break
    

cam.release()
cv2.destroyAllWindows()