


import time
import serial

print("Rx.....")

ser = serial.Serial("/dev/ttyS0", baudrate=9600)
time.sleep(1)
ser.flushInput()
try:
    while True:
        if ser.inWaiting() > 0:
            data = ser.read(5)
            print("working")
            print(data)

except KeyboardInterrupt:
    ser.flushInput()
    print("Exiting Program")
    


