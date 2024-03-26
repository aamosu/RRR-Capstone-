# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import serial
import time


ser = serial.Serial("/dev/ttyS0",9600,timeout=1)

ser.flushInput()

data = ""
while 1: 
    #while ser.inWaiting() > 0:
     #   data += ser.read(ser.inWaiting())
    #time.sleep(6)
    data=ser.read()
    #if data != "":
     #   for i in range(len(data)):
    print (data)
       # print ("")
       # data = ""
