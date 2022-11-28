#from imutils import paths #imutils includes opencv function
import cv2
import os
import pickle
import numpy as np

import face_recognition


#get paths of each file in folder named Images
#Images here that contains data(folders of various people)
entries = os.listdir('./')
print(entries)
entries1 = os.listdir('./harsh.agrawal2274@gmail.com')
entries2 = os.listdir('./manansoni.soni77@gmail.com')
print(entries1)
print(entries2)


kEncodings=[]
kNames=[]

Name="harsh.agrawal2274@gmail.com"
out_arr=np.zeros((128,), dtype=int)

for (i,ip) in enumerate(entries1):
    # extract the person name from the image path
    name = ip.split(".")[0]
    main= './harsh.agrawal2274@gmail.com/'+ip
    image = cv2.imread(main)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    # compute the facial embedding for the any face 
    encodings = face_recognition.face_encodings(rgb, boxes)

    out_arr = np.add(out_arr, encodings)  
    #kEncodings.append(encodings)
    #kNames.append(name)
#save emcodings along with their names in dictionary data
print(out_arr)
out_arr=out_arr/len(entries1)
kEncodings.append(out_arr)
kNames.append(Name)

Name="manansoni.soni77@gmail.com"
out_arr=np.zeros((128,), dtype=int)
for (i,ip) in enumerate(entries2):
    # extract the person name from the image path
    name = ip.split(".")[0]
    main= './manansoni.soni77@gmail.com/'+ip
    image = cv2.imread(main)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    boxes = face_recognition.face_locations(rgb)
    # compute the facial embedding for the any face 
    encodings = face_recognition.face_encodings(rgb, boxes)
    out_arr = np.add(out_arr, encodings)  
    #kEncodings.append(encodings)
    #kNames.append(name)
#save emcodings along with their names in dictionary data

out_arr=out_arr/len(entries1)
kEncodings.append(out_arr)
kNames.append(Name)

data = {"encodings": kEncodings, "names": kNames}
#use pickle to save data into a file for later use

f = open("face_enc.txt", "wb")
f.write(pickle.dumps(data))#to open file in write mode
f.close()#to close file