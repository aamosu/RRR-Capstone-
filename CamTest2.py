#importing numpy 
import sys
import numpy as np 
# importing cv2 
import cv2
import time
import serial
import struct 


ser = serial.Serial("/dev/ttyS0",9600,timeout=1)
time.sleep(1)
ser.flushOutput()

# path 
path = r'/home/recovery-robot/rrrTestimg'
  
# Reading an image in default mode 
testImageOg = cv2.imread(path) 
testImage=cv2.resize(testImageOg,(800,800))
  
# Window name in which image is displayed 
window_name = 'testImage'

cv2.imshow(window_name,testImage)
cv2.waitKey(0)
cv2.destroyAllWindows()



#greyImage=np.zeros((len(image),len(image[0]),3),np.uint8)

#for x in image:
#	for y in image[0]:

'''
greyImage[:,:,0]=np.ones([len(image),len(image[0])])*image[:,:,0]
greyImage[:,:,1]=np.ones([len(image),len(image[0])])*image[:,:,1]
greyImage[:,:,2]=np.ones([len(image),len(image[0])])*image[:,:,2]
print("DONE")		
		
cv2.imshow('grey',greyImage)
cv2.waitKey(0)

cv2.destroyAllWindows()
		
'''
arrImage=np.array(testImage)
arrImage=arrImage.astype(int)
imageData=np.array(testImage)

term = "DONE"

try: 
	for x in range(len(testImage)):
		for y in range(len(testImage[0])):
				R=imageData[x,y,0]
				G=imageData[x,y,1]
				B=imageData[x,y,2]
				packet= str(x) + ','+ str(y)+ ','+str(R) +','+ str(G) +','+ str(B)+"\n" 
				ser.write(packet.encode("utf-8"))


	ser.write(term.encode("utf-8"))

except KeyboardInterrupt:
 ser.flushOutput()
 print("Exiting Program")





