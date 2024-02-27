#Receiver code starts here
import time
import serial
import struct 
#import board 
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
#GPIO.output(23, 0) 
#GPIO.output(24, 0) 
lora = serial.Serial('/dev/ttyS0', baudrate=9600)
#time.sleep(1)

while True:
    try:
        if lora.inWaiting() > 0:
                #print ('here')
            received_data = lora.read(8)  
            buff=received_data  
            data= struct.unpack('d',buff)          #read serial port
            time.sleep(2)
            print (data)                   #print received data
                #lora.write(received_data)
           # print ('here2')                #transmit data serially 
    #lora.close()
    except KeyboardInterrupt:
        print("exit")
        lora.close()
        
        

#Receiver code ends here
