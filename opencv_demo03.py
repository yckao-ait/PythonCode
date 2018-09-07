#! Python 3 
# opencv_demo03.py
# 09/07/2018 sample created
#--------------------------
import os
import cv2
import glob

basedir = os.path.abspath(os.path.dirname(__file__))
os.chdir(basedir)

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,-1)
    #re=cv2.resize(img,(200,100))
    re=cv2.resize(img,(int(img.shape[1]/6),int(img.shape[0]/6)))
    cv2.imshow(image,re)
    cv2.imwrite("resized_"+image,re)

cv2.waitKey(0)
cv2.destroyAllWindows()
