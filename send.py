# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import time
import struct 

ser1 = serial.Serial("/dev/ttyS0",9600,timeout=1)

time.sleep(1)




while 1:
    time.sleep(1)
    s = 1.23
    data= ser1.write(struct.pack('f',s))
    print(data) 


ser1.flush()
