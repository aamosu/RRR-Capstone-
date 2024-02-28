
import time
import serial

print("Sending Message.....")

# Open serial connection
ser = serial.Serial("/dev/ttyS0", baudrate=9600)
#time.sleep(1)  # Wait for the serial connection to initialize
temp = 490012345678
ser.flushOutput()
try:
    while True:
            
            buff=str(temp)
            time.sleep(3)
            print(ser.write(buff.encode()))
            

except KeyboardInterrupt:
    print("Exiting Program")
    # Close serial connection
    ser.close()



