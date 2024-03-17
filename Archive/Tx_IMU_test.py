import time
import serial


print("Sending Message.....")

ser = serial.Serial("/dev/ttyS0", baudrate=9600)
time.sleep(1)
while True:
    #time.sleep(5)
    temp='Aaliah'
    encoded_temp = temp.encode('ascii')
    temp_bytes = temp.encode('utf-8')
    ser.write(encoded_temp)
    time.sleep(3)
   


    
    
#while loop constantly read values from IMU and while loop constantly transmit the values currently held
#temp encode will change because IMU wont be a preset string?
#enable I2C in sudo raspi-config



