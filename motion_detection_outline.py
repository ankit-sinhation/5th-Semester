#!/usr/bin/python3
import cv2
import numpy as np
# capture 
cap=cv2.VideoCapture(0)
while True:
    # reading frame
    status,frame=cap.read()
    status,frame1=cap.read()
    #  image difference 
    dimg=cv2.absdiff(frame,frame1)
    #  gray of diff images
    grayd=cv2.cvtColor(dimg,cv2.COLOR_BGR2GRAY)
    # gaussianblur in the image
    blur=cv2.GaussianBlur(grayd,(5,5),0)
    # threshold image
    ret,ths=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    # dialated image
    dilated=cv2.dilate(ths,np.ones((3,3),np.uint8),iterations=3)
    # finding and applying coutours
    img,c,h=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,c,-1,(0,0,255),2)
    cv2.imshow('original',frame)
    cv2.imshow('diff',frame1)
    if  cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
