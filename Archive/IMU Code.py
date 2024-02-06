# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.
import time
import board
import adafruit_lsm9ds1
import busio
import serial

# Create sensor object, communicating over the board's default I2C bus
i2c = busio.I2C(board.SCL, board.SDA)  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)
ser = serial.Serial("/dev/ttyS0", baudrate=9600)
time.sleep(1)

print("Sending Message.....")

while True:
    # Read acceleration, magnetometer, gyroscope, temperature.
    #accel_x, accel_y, accel_z = sensor.acceleration
    #mag_x, mag_y, mag_z = sensor.magnetic
    #gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.

    #print("Temperature: {0:0.3f}C".format(temp))
    
    # Delay for a second.
    #time.sleep(1.0)

    try:
        ser.flushOutput()
        #time.sleep(5)
        buff=str(temp)
        ser.write(buff.encode('iso-8859-15'))
        


    except KeyboardInterrupt:
        print("Exiting Program")
    
