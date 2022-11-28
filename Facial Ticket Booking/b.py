import cv2
import os
import pickle
import numpy as np
import data
import face_recognition

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot detect Webcamp")
 
lis=[]
while True:
    ret,frame=cap.read()
    cv2.imshow('Input',frame)
    c=cv2.waitKey(1)
    if c==27:
        break
    if c==32:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb)
        # compute the facial embedding for the any face 
        encodings = face_recognition.face_encodings(rgb, boxes)
        lis.append(encodings)
        #print("Image captured")
cap.release()
cv2.destroyAllWindows()

mails=[]
with open ('./face_enc.txt','rb') as fp:
    tasks=pickle.load(fp)

for i,ip in enumerate(lis):
    op=10000000000
    p=0
    for m in ip:
        ll=0
        for j,jk in enumerate(tasks["encodings"]):       
            dist = np.linalg.norm(m-jk)
            if (dist < op ):
                k=ll
                op=dist
            ll+=1
        #print(i,":",p,":",tasks["names"][k])
        #print(tasks["names"][k])
        mails.append(tasks["names"][k])
        p+=1

#print(mails)
data.mail_ch(mails)