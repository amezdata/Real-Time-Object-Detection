# Real-Time Object Detection
# By R.H. Amezqueta 


import math
from cv2 import MARKER_CROSS
import numpy as np
import cv2 as cv

# Defines external camera
cam = cv.VideoCapture(0)

while True: 
    ret, frame = cam.read(1)
    # Image size
    width = int(cam.get(3))
    height = int(cam.get(4))
    # Frame cropping
    frame_cropped = frame[0:1000, 300:1620]
    gray_frame = cv.cvtColor(frame_cropped, cv.COLOR_BGR2GRAY) # Gray frame
    ret, threshold = cv.threshold(gray_frame, 70, 255, cv.THRESH_BINARY) # 70, 255 threshold value 
    
    # Detects object contours
    contours, hierarchy = cv.findContours(threshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours: 
        (x, y, w, h) = cv.boundingRect(cnt) # Object bounding coordinate
        area = cv.contourArea(cnt) # Area in pixels
        diameter = math.sqrt((area/32.94)/3.14) * 2 # Conversion scale to mm2 + diameter (pi is set to 3.14)
        font = cv.FONT_ITALIC

        # Adds text annotations to the cropped frame
        cv.putText(frame_cropped, "D: " + str(diameter)[:5] + 'mm', (x-5, y-15), 1, 2, (255,255,255)) 
        cv.putText(frame_cropped, "Objects detected: " + str(len(contours)), (25, 50), 2, 2, (255,255,255)) 

        # Draws circles on the cropped frame based on the diameter of detected objects.
        if diameter > 20:
            cv.circle(frame_cropped, (x+(w//2), y+(h//2)), h//2, (0,255,0), 2) 
        else:
            cv.circle(frame_cropped, (x+(w//2), y+(h//2)), h//2, (0,0,255), 2)

    cv.imshow('Belt frame', frame_cropped) # Displays the cropped image
    cv.imshow('Belt threshold', threshold) # Displays the threshold of the cropped image
    
    if cv.waitKey(1) == ord('q'): # Closing criterion
        break

cam.release()
cv.destroyAllWindows()
