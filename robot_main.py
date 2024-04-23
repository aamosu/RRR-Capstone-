from Sensors.LoRa.LoRacomm import LoRaComm
import time
import serial

class RobotMain:
    def __init__(self):
        self.lora = LoRaComm('/dev/ttyS0')  # Adjust the LoRa serial port accordingly
        self.usb_serial = serial.Serial('/dev/ttyACM1', 9600, timeout=1)  # USB serial port

    def run(self):
        while True:
            # Removed sleep here to make response quicker, adjust based on your need
            data = self.lora.readline().decode().strip()  # Read data from LoRa
            print(data)
            if data:
                self.process_data(data)

    def process_data(self, data):
        if data:  # Check if data is not empty
            command = data[0]  # First character of the received data
            #print(command)
            if command == 'B':
                #print("Backward command received")
                print(self.usb_serial.write(b'B\n')) # Send 'B' over USB serial
            elif command == 'F':
                #print("Forward command received")
                print(self.usb_serial.write(b'F\n'))  # Send 'F' over USB serial
            elif command == 'R':
                #print("Forward command received")
                print(self.usb_serial.write(b'R\n'))  # Send 'R' over USB serial
            elif command == 'L':
                #print("Forward command received")
                print(self.usb_serial.write(b'L\n') ) # Send 'L' over USB serial
            else:
                # Handle unknown command
                print("Unknown command:", data)

if __name__=="__main__":
    robot = RobotMain()
    robot.run()

