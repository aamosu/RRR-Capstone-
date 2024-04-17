# -*- coding:utf-8 -*-
import serial
import time

# Open serial port
ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)
ser.flushInput()

# Main loop
while True:
    # Check if there's data available to read
    while ser.inWaiting() > 0:
        # Read one byte at a time
        data = ser.read(4)
        # Print the received byte
        print(data)
    # Add a delay to prevent busy-waiting
    time.sleep(0.1)

