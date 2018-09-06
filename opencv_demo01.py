import os
import cv2
import time

tp101_1="remi-yuan-569408-unsplash.jpg"

####################################################
# setup default font file name
basedir = os.path.abspath(os.path.dirname(__file__))
imgFileName = os.path.join(basedir,tp101_1)

img=cv2.imread(imgFileName,-1)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img=cv2.resize(img,(1000,500))
cv2.imshow("Taipei 101",resized_img)
cv2.waitKey(0)

#time.sleep(30)
cv2.destroyAllWindows()