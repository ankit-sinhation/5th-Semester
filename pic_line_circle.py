#!/usr/bin/python3

import cv2

#all functions of cv2 that is opencv model
#print dir(cv2)

#reading image
#   image name, image features
#       we can write  cv2.IMREAD_COLOR instead of 1
#       we can write  cv2.IMREAD_BGR2GRAY instead of 2
#       we can write  cv2.IMREAD_UNCHANGE_COLOR instead of -1
img=cv2.imread("leo.jpg")
#   to draw a line in dog image
#       imagedata , start point, end point, color, line width<cm/mm>
cv2.line(img,(0,0),(150,200),(0,0,225),10)
cv2.rectangle(img,(20,20),(100,100),(123,25,200),6)
cv2.circle(img,(100,100),30,(12,45,67),3)
#   deciding font type
##font=cv2.FONT_HERSHEY_SIMPLEX
#   putting text  in image
#           data, text, starting point, fonttype, size, color
#cv2.putText(img,"DOGGG",(10,10),font,3,(100,23,200),cv2.LINE_AA)
# if we will use -1 instead of 6, then it will fill the color inside the rect.
# if we will use 0 instead of 6, then it will fill black color inside the rect.
# if we will use -1 instead of 255(max. range of the image), then it will fill  the white color inside the rect.
   
cv2.imshow("lineimg",img)
cv2.imwrite("Dogline.jpeg",img)
cv2.waitKey(0)

