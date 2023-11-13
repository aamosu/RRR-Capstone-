#Receiver code starts here
import time
import serial
#import board 
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.output(23, 0) 
#GPIO.output(24, 0) 
lora = serial.Serial('/dev/ttyAMA0', baudrate=9600)
time.sleep(1)

if lora.inWaiting() > 0:
    received_data = lora.read()              #read serial port
    time.sleep(1)
    print (received_data)                   #print received data
    #lora.write(received_data)                #transmit data serially 
    lora.close()


#Receiver code ends here
