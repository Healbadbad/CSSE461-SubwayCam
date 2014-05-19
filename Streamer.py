import urllib
import cv2
import numpy as np
class Streamer():
    def __init__(self):
        self.history = b'';
        self.stream=urllib.urlopen('http://subway-cam.rose-hulman.edu/stream.jpg')
        self.bytes = self.stream.read(35628)
        #print self.bytes
        a = self.bytes.find('\xff\xd8')
        b = self.bytes.find('\xff\xd9')
        #print a,b
        
    def read(self):
        i = ''
        self.jpg = '';
        self.bytes+=self.stream.read(35628)
        #print self.bytes
        a = self.bytes.find('\xff\xd8')
        b = self.bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            #print 'found the image in the stream'
            self.jpg = self.bytes[a:b+2]
            self.bytes= self.bytes[b+2:]
        i = cv2.imdecode(np.fromstring(self.jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        return 1,i
            #cv2.imshow('i',i)
            #if cv2.waitKey(1) ==27:
                #exit(0) 
                
    def record(self):
        i = ''
        self.jpg = '';
        self.bytes+=self.stream.read(35628)
        #self.history +=self.bytes
        #print self.bytes
        a = self.bytes.find('\xff\xd8')
        b = self.bytes.find('\xff\xd9')
        if a!=-1 and b!=-1:
            #print 'found the image in the stream'
            self.jpg = self.bytes[a:b+2]
            self.bytes= self.bytes[b+2:]
        i = cv2.imdecode(np.fromstring(self.jpg, dtype=np.uint8),cv2.CV_LOAD_IMAGE_COLOR)
        self.history +=i
        return 1,i
            #cv2.imshow('i',i)
            #if cv2.waitKey(1) ==27:
                #exit(0) 
    def stoprecord(self):
        
        countfile = open('count.txt','wr')
        count = int(countfile.read())
        count +=1
        countfile.close()
        countfile = open('count.txt','w')
        countfile.write(str(count))
        tag = 'video'+str(count)
        file = open(tag,'w')
        file.write(self.history)
        file.close()