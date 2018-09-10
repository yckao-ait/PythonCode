#! Python 3 
# opencv_demo04_facedet.py
# 09/10/2018 sample created
#--------------------------
import os
import cv2

photo1="andrew-haimerl-381937-unsplash.jpg"
photo2="andrew-haimerl-597717-unsplash.jpg"

####################################################
# setup default font file name
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread(photo1)
res_img=cv2.resize(img,(int(img.shape[1]/6),int(img.shape[0]/6)))
gray_img = cv2.cvtColor(res_img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

for x,y,w,h in faces:
    img = cv2.rectangle(res_img,(x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

cv2.imshow("Got it",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
