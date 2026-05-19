# Import required libraries

import numpy as np          # Used for numerical operations and image arrays
import cv2                  # OpenCV library for computer vision tasks
import imutils              # Helper functions for image processing
import datetime             # Used for date and time operations


# Load the Haar Cascade XML file
# This file contains the trained object detection model

gun_cascade = cv2.CascadeClassifier('cascade.xml')


# Start webcam capture
# '0' means the de+fault webcam

camera = cv2.VideoCapture(0)


# Variable to store the first frame
# Often used in motion detection systems

firstFrame = None


# Variable to track whether a gun/object is detected
# Initially set to None

gun_exist = None

while True:
    ret,frame = camera.read()
    frame = imutils.resize(frame,width=500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray,
                                       1.3,5,
                                        minSize=(100,100))

    if len(gun)>0:
        gun_exist=True

    for (x,y,w,h) in gun:
        frame = cv2.rectangle(frame,
                              (x,y),
                              (x+w,y+h),
                              (255,0,0),2)

        roi_gray=gray[y : y+h, x : x+w]
        roi_color=frame[y:y+h , x:x+w]

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        break


if gun_exist:
    print("Gun Detected.....")

else:
    print("Guns didn't detected......")

camera.release()
cv2.destroyAllWindows()