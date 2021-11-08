# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 23:15:55 2021

@author: mohwa
"""

import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

img = cv2.imread("images/2.jfif")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
gray,
        
scaleFactor=1.2,
minNeighbors=3
,     
minSize=(20, 20)
)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    
        
# width = 500
# height = 620
# points = (width, height)
# resized_up = cv2.resize(img, points, interpolation= cv2.INTER_LINEAR)

cv2.imshow("image",img)
cv2.waitKey(0)