import cv2
import numpy as np
import matplotlib.pyplot as plt
#http://matplotlib.org/users/gridspec.html
im = cv2.imread("pics\\SW1.png")
fig,ax = plt.subplots(2,2)
matim = cv2.cvtColor(im, cv2.cv.CV_BGR2RGB)
ax[0,0].imshow(matim)
ax[0,1].hist(im.flatten(), 256, range=(0,255))
plt.show()