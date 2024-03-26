import os
from picamera import PiCamera
import numpy as np
import sys

import cv2  



os.system("libcamera-jpeg -o test1.jpg -t 2000 --width 2592 --height 1944")

# path 
path = r'/home/recovery-robot/test1.jpg'
  
# Reading an image in default mode 
image = cv2.imread(path) 
  
# Window name in which image is displayed 
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image) 

# waits for user to press any key 
# (this is necessary to avoid Python kernel form crashing) 
cv2.waitKey(0) 
  
# closing all open windows 
cv2.destroyAllWindows() 

#Blank Image
recImg= np.zeros((len(image),len(image[0]),3), np.uint8)

#Test Array for packet 
sentPackets= np.empty((len(image),len(image[0]),3))
