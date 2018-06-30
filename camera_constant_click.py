#!/usr/bin/python3

import cv2

#   to start web or external web camera
capture=cv2.VideoCapture(0)
#   number of camera connected to system. 0 is system's camera by default.
#capture.isOpened()
#true
#capture.release()
#capture.isOpened()
#False

if      capture.isOpened() :
        print ("Camera is ready to take picture")
#       current camera data, aftr frame take camera status
        status,frame=capture.read()
        cv2.imshow("frame1",frame)
        cv2.waitKey(0)
        capture.release()
else :
        print ("check your camera drivers with OS")
