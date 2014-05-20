import numpy as np
import cv2
import Streamer
import matplotlib.pyplot as plt

#fig,ax = plt.subplots(2,2)
#ax[0,0].imshow(matim)
#ax[0,1].hist(im.flatten(), 256, range=(0,255))
#plt.show()


c = Streamer.Streamer()
#c = cv2.VideoCapture('output.avi')
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
back = cv2.imread('cap.png')
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('outputlarge.avi',fourcc, 20.0, (640,480))
i=20
while(1):
    try:
    
        _,f = c.read()
         
        cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,0.0001)
         
        res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)
        diff = cv2.absdiff(f,res2)
        
        diffg = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
        diffc = cv2.cvtColor(diffg,cv2.COLOR_GRAY2BGR)
        
        #Histogram
        hists = np.zeros((480,640,3))
        b,g,r = cv2.split(f)
        bins = np.arange(640).reshape(640,1)
        color = [(255,0,0),(0,255,0),(0,0,255)]
        
        for item,col in zip([b,g,r],color):
            hist_item = cv2.calcHist([item],[0],None,[640],[0,640])
            cv2.normalize(hist_item,hist_item,0,480,cv2.NORM_MINMAX)
            hist = np.int32(np.around(hist_item))
            pts = np.column_stack((bins,hist))
            cv2.polylines(hists,[pts],False,col)
        hists=np.flipud(hists)
    
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
        canvas[480:,:640] = res2
        canvas[480:,640:] = hists
        
        #cv2.imshow('img',f)
        #cv2.imshow('avg1',res1)
        #cv2.imshow('subtractedgray',diffg)
        #cv2.imshow('avg2',res2)
        cv2.imshow('Images',canvas)
        k = cv2.waitKey(20)
        #out.write(canvas)
        if k == 27:
            break
        if k == ord('s'):
            cv2.imwrite('canvas'+str(i)+'.png',canvas)
            #cv2.imwrite('capturebg'+str(i)+'.png',diffc)
            #cv2.imwrite('capturediff'+str(i)+'.png',res2)
            i+=1
    except:
        pass

#cv2.destroyAllWindows()
c.release()