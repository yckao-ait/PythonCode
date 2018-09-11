#! Python 3 
# opencv_demo05_face_eye_det.py
# 09/11/2018 sample created
#--------------------------
import os
import cv2

photo1="andrew-haimerl-381937-unsplash.jpg"
photo2="andrew-haimerl-597717-unsplash.jpg"
photo3="jodyhongfilms-279698-unsplash.jpg"
photo4="erik-lucatero-310633-unsplash.jpg"

####################################################
# setup default font file name
basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")

img=cv2.imread(photo4)
res_img=cv2.resize(img,(int(img.shape[1]/8),int(img.shape[0]/8)))
gray_img = cv2.cvtColor(res_img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

for (x,y,w,h) in faces:
    res_img = cv2.rectangle(res_img,(x,y),(x+w,y+h),(255,0,0),2)
    
    roi_gray  = gray_img[y:y+h, x:x+w]
    roi_color = res_img[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

print(type(faces))
print(faces)

cv2.imshow("Face & Eye Detection",res_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
