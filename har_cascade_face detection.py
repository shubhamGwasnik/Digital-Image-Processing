import cv2
import numpy as np
img=cv2.imread('istockphoto-1146473249-612x612 (1).jpg')
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv.imshow('image',img)
# cv.imshow('gray_img',gray_img)
haar_cascade=cv2.CascadeClassifier('face.xml')

faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.2, minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv2.imshow('Detected Faces', img)

cv2.waitKey(0)


## har cascade are more prone to noise
# DELIMBS IS BETTER