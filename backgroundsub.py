import numpy as np
import cv2
import Streamer
import matplotlib.pyplot as plt

fig,ax = plt.subplots(2,2)
#ax[0,0].imshow(matim)
#ax[0,1].hist(im.flatten(), 256, range=(0,255))
#plt.show()


#c = Streamer.Streamer()
c = cv2.VideoCapture('output.avi')
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
    diffc = cv2.cvtColor(diffg,cv2.COLOR_GRAY2BGR)

#DISPLAY SETUP
    canvas = np.zeros((480*2,640*2,3),np.uint8)
    
#DISPLAYING

    #ax[0,0].imshow(matim)
    #ax[1,0].hist(matim.flatten(), 256, range=(0,255))
    #ax[0,1].imshow(diffg)
    #ax[1,1].hist(diffg.flatten(), 256, range=(0,255))
    #plt.show(1)
    
    canvas[:480,:640] = f
    canvas[:480,640:] = diffc
    canvas[480:,:640] = res1
    canvas[480:,640:] = res2
    
    #cv2.imshow('img',f)
    #cv2.imshow('avg1',res1)
    #cv2.imshow('subtractedgray',diffg)
    #cv2.imshow('avg2',res2)
    cv2.imshow('Images',canvas)
    k = cv2.waitKey(20)
 
    if k == 27:
        break
    if k == ord('s'):
        cv2.imwrite('cap2.png',f)

#cv2.destroyAllWindows()
c.release()