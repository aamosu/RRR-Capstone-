
import time
import board
import adafruit_lsm9ds1
import busio
import serial
import struct 
import numpy as np 

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA

sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
ser = serial.Serial("/dev/ttyS0",9600,timeout=1)
time.sleep(1)
ser.flushOutput()

print("Sending Message.....")

count=0
try:
    while True:
     
        temp = sensor.temperature
        
        gyro_x, gyro_y, gyro_z = sensor.gyro
        buff=[gyro_x, gyro_y, gyro_z,count]
        time.sleep(2)
        float_round = [np.round(buff,6) for x in buff]
        string_float = [ str(float_round[0]) for x in float_round[0]]
        string_float[0]=string_float.append("\n")
        time.sleep(2)
        count=count+1
        print("working")
        ser.write(string_float[2].encode())
        

except KeyboardInterrupt:
    ser.flushOutput()
    print("Exiting Program")
    
