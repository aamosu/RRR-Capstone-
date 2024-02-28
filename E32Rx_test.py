import time
import serial
import struct 

print("Rx.....")

ser = serial.Serial("/dev/ttyS0",9600,timeout=1)
ser.reset_input_buffer()

while True:
    try:
            

                #time.sleep(5)
                data=bytes(ser.read(4)) # Reads in 4 Bytes 
                print(struct.unpack('f',data)) # Unpacks transmitted mgs and prints
            
    except KeyboardInterrupt:
        print("Exiting Program")

            
            
            
            
            
            
            
            
            
                #ser.reset_input_buffer()
            #ser.flushInput()
            #print("working")
            #ser.reset_input_buffer()
            #data = ser.readline(6).decode('utf-8')
            #ser.reset_input_buffer()
            #data=ser.read(6).decode('utf-8')
                        #print(data)
            #time.sleep(1)
