import numpy as np
import cv2
import Streamer

c = Streamer.Streamer()
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
back = cv2.imread('cap.png')

while(1):
    _,f = c.read()
     
    cv2.accumulateWeighted(f,avg1,0.1)
    cv2.accumulateWeighted(f,avg2,0.00001)
     
    res1 = cv2.convertScaleAbs(avg1)
    res2 = cv2.convertScaleAbs(avg2)
    diff = cv2.absdiff(f,res2)
    
    diffg = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    cv2.imshow('img',f)
    #cv2.imshow('avg1',res1)
    cv2.imshow('subtractedgray',diffg)
    cv2.imshow('avg2',res2)
    k = cv2.waitKey(20)
 
    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite('cap2.png',f)
 
cv2.destroyAllWindows()
c.release()