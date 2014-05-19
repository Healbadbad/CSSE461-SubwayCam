import numpy as np
import cv2
import Streamer
import matplotlib.animation as ani
import matplotlib.pyplot as plt

fig,ax = plt.subplots(2,2)
#c = Streamer.Streamer()
c = cv2.VideoCapture('output.avi')
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
back = cv2.imread('cap.png')
#ax[0,0].imshow(matim)
#ax[1,0].hist(matim.flatten(), 256, range=(0,255))
#ax[0,1].imshow(diffg)
#ax[1,1].hist(diffg.flatten(), 256, range=(0,255))

def updatefig(*args):
    try:
        print "updating images"
        _,f = c.read()
        plt.cla()
        '''
        cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,0.00001)
         
        res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)
        diff = cv2.absdiff(f,res2)
        
        diffg = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    '''
    #DISPLAY SETUP
        matim = cv2.cvtColor(f, cv2.cv.CV_BGR2RGB)
        
    #DISPLAYING
        ax[0,0].imshow(matim)
        
        '''
        ax[1,0].hist(matim.flatten(), 256, range=(0,255))
        ax[0,1].imshow(diffg)
        ax[1,1].hist(diffg.flatten(), 256, range=(0,255))
        '''
    
    except:
        pass
    print 'returning'
    return ax
    
anim = ani.FuncAnimation(fig, updatefig,interval =50)#initfunc=init

plt.ioff()
plt.show()
c.release()