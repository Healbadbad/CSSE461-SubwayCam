import numpy as np
import cv2
import Streamer

cap = cv2.VideoCapture('output.avi')

fgbg = cv2.BackgroundSubtractorMOG2()()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('BG',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()