
import time
import serial
from time import sleep
import struct 

#GPIO.setwarnings(False)
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)


print("Sending Message.....")

ser = serial.Serial("/dev/ttyS0", baudrate=9600)
time.sleep(1)

try:

        time.sleep(1)
        #temp=1
        ser.write(struct.pack('f',1.23))
        #sleep(1)

    

except KeyboardInterrupt:
    print("Exiting Program")

