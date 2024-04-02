import numpy as np
import time
import csv
import serial

from Sensors.LoRa.LoRacomm import loRaComm

class  robotMain:
    lora = loRaComm('COM7') #need to specify the serial port


    while True: 
        lora.read() #read info from LoRa 

        def process_data(self, data):
            if data:  # Check if data is not empty
                command = data[0]  # First character of the received data
                if command == 'R':
                    print(" R")
                    rightMove()
                elif command == 'L':
                    print("L")
                elif command == 'B':
                    print("B")
                elif command == 'F':
                    print("F")
                elif command == 'C':
                    print("G")
                else:
                    # Unknown command
                    print("Unknown command:", command)


