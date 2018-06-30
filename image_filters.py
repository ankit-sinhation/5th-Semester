#!/usr/bin/python3

import cv2

img=cv2.imread('redhat.jpg')
# bgr to hsv
imghsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# only redimage with masking 
maskimg=cv2.inRange(imghsv,(50,50,110),(255,255,130))

# bitwise mask and original image
redimg=cv2.bitwise_and(img,img,mask=maskimg)
cv2.imshow('ori',img)
cv2.imshow('hsv',imghsv)
cv2.imshow('mask',maskimg)
cv2.imshow('red',redimg)

cv2.waitKey(0)

cv2.destroyAllWindows()
