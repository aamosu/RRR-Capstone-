
import time
import board
import adafruit_lsm9ds1
import busio
import serial
import struct 

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA

sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
ser = serial.Serial("/dev/ttySC0",115200,timeout=1)
time.sleep(1)

print("Sending Message.....")


while True:
 
 
    #gyro_x, gyro_y, gyro_z = sensor.gyro
    
    #grabs temp values 
    
    temp = sensor.temperature

    try:

        #stores temp
        buff=temp
        
        #writes temp 
        time.sleep(1)
        ser.write(struct.pack('f',buff))
        
        
        
        
        
        
    except KeyboardInterrupt:
        print("Exiting Program")
    
