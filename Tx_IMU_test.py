import time
import serial


print("Sending Message.....")

ser = serial.Serial("/dev/ttyS0", baudrate=9600)
time.sleep(1)
try:
    #time.sleep(5)
    temp='Aaliah'
    encoded_temp = temp.encode('ascii', 'utf-8')
    temp_bytes = temp_str.encode('utf-8')
    #ser.write(bytes(temp))
   

except KeyboardInterrupt:
        print("Exiting Program")
    
    
#while loop constantly read values from IMU and while loop constantly transmit the values currently held
#temp encode will change because IMU wont be a preset string?
#enable I2C in sudo raspi-config



