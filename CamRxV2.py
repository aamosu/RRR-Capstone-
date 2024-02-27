
import time
import serial
import csv
import numpy as np

print("Rx.....")

ser = serial.Serial("/dev/ttyS0", baudrate=9600,timeout=1)
time.sleep(1)
ser.flushInput()


recImg=np.empty(10)
index=0

data_array=[]

try:
    while True:
                if ser.inWaiting() > 0:
                    time.sleep(1)
						#if index<283452:
                    data = ser.readline().decode().strip()
						#np.insert(recImg,index,int(data.decode()))
						#print (data.decode.split(','))
                    dataString=str(data)
                    print(dataString)
                    if dataString:
                        data_array.append(dataString.split(','))
                        #print(f"Received data: {data_array}")
						#print (dataString.split(','))
						#print()
								#index=index+1
						#else:
								#break
						#print(data)

except KeyboardInterrupt:
	#print(recImg)
    ser.flushInput()
    print("Exiting Program")
    ser.close()
    
