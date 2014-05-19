'''
Created on Apr 25, 2014

@author: blanknc
'''
import numpy as np
import cv2

print "Should be 2.4.8.1 - " + cv2.__version__
cap = cv2.VideoCapture(0)
ret,frame_old=cap.read()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    canvas = np.zeros((480,640*2,3),np.uint8)
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(frame_old, cv2.COLOR_BGR2GRAY) 
    
    #Generate Histograms
    hists = np.zeros((480,640,3))
    b,g,r = cv2.split(frame)
    bins = np.arange(640).reshape(640,1)
    color = [(255,0,0),(0,255,0),(0,0,255)]
    
    for item,col in zip([b,g,r],color):
        hist_item = cv2.calcHist([item],[0],None,[640],[0,255])
        cv2.normalize(hist_item,hist_item,0,480,cv2.NORM_MINMAX)
        hist = np.int32(np.around(hist_item))
        pts = np.column_stack((bins,hist))
        cv2.polylines(hists,[pts],False,col)
    hists=np.flipud(hists)
    
    flow = cv2.calcOpticalFlowFarneback(gray2,gray,0.5,1,3,15,3,5,1)
    try:
        #cv2.cv.Copy(gray,blank_image)
        canvas[:480,:640] = frame
        canvas[:480,640:] = hists
        
        pass
    except:
        pass
    # Display the resulting frame
    cv2.imshow('frame',canvas)
    cv2.imshow('optflow',flow)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    #cv2.cv.Copy(frame, frame_old)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()