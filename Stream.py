'''
Created on Apr 25, 2014

@author: blanknc
'''

import cv2
import urllib 
import numpy as np
import Streamer
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output2.avi',fourcc, 20.0, (640,480))

#stream = urllib.urlopen('http://subway-cam.rose-hulman.edu/stream.jpg')
cam = Streamer.Streamer()
while True:
    try:
        _,i = cam.read() 
        out.write(i)
        cv2.imshow('i', i)
        if cv2.waitKey(1) == 27:
            #cam.stoprecord()
            exit(0) 
    except:
        pass

out.release()