import cv2
import numpy as np
import os
import fnmatch
import time

# define number of camera device connected to host
devices = os.listdir("/dev")
for dev in devices:
    if fnmatch.fnmatch(dev, "video*"):
        camera_num = int(dev[-1])
        break

# create object cap for capturing from video device /dev/videox
cap = cv2.VideoCapture(camera_num)

cap.set(3, 1280)
cap.set(4, 720)

# set resolution properties for object cap to full hd
frame_width = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
frame_heidht = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

print frame_width
print frame_heidht

fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
footage = cv2.VideoWriter("footage.mov", fourcc, 30, (frame_width, frame_heidht))

# define font for display time on video stream
font = cv2.FONT_HERSHEY_SIMPLEX

while(True):
    # check if device for capturing is opened
    if cap.isOpened() is not True:
        # open if not
        cap.open(camera_num)
        ret, frame = cap.read()
    else:
        # read frame if device is opened
        ret, frame = cap.read()
    # apply convert color to a frame

    # add time and device to footage
    cv2.putText(frame, time.ctime(), (frame_width - 230,
                                      frame_heidht - 20),
                font, 0.5, (255, 255, 255), 1, cv2.CV_AA)
    cv2.putText(frame, "/dev/" + dev,
                (frame_width - 350, frame_heidht - 20),
                font, 0.5, (255, 255, 255), 1, cv2.CV_AA)

#    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    footage.write(frame)
    # show processed frame
    cv2.imshow('opencv-show', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# release capture object
cap.release()
footage.release()
# close all windows
cv2.destroyAllWindows()
