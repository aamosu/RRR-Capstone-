import time
import serial
from Sensors.LoRa.LoRacomm import *

threshold = 20

class ObjectAvoid:
    def __init__(self):
        self.ser = loRaComm('/dev/ttyACM1')
        self.frontDistance = 0
        self.leftDistance = 0
        self.rightDistance = 0

    def go_forward(self):
        self.ser.writeRobot('F')

    def turn_left(self):
        self.ser.writeRobot('L')

    def turn_right(self):
        self.ser.writeRobot('R')

    def go_backward(self):
        self.ser.writeRobot('B')

    def stop_motors(self):
        self.ser.writeRobot('S')

    def check_and_drive_front(self):
        while self.frontDistance < threshold:
            self.stop_motors()
            if self.rightDistance < threshold and self.leftDistance > threshold:
                self.turn_left()
                self.check_and_turn_right()
            elif self.leftDistance < threshold and self.rightDistance > threshold:
                self.turn_right()
                self.check_and_turn_left()
            elif self.rightDistance > threshold and self.leftDistance > threshold:
                self.turn_right()
                self.check_and_turn_left()
            else:
                self.go_backward()
                if self.rightDistance > threshold:
                    self.turn_right()
                    self.check_and_turn_left()
                elif self.leftDistance > threshold:
                    self.turn_left()
                    self.check_and_turn_right()
        self.go_forward()

    def check_and_turn_right(self):
        while self.rightDistance < threshold:
            self.update_sensors()
            self.go_forward()
        self.turn_right()

    def check_and_turn_left(self):
        while self.leftDistance < threshold:
            self.update_sensors()
        self.go_forward()
        self.turn_left()

    def update_sensors(self):
        for _ in range(3):
            line = self.ser.readline().decode("utf-8").rstrip()
            if not line:
                continue
            sensor_loc = line[0]
            data = int(line[1:])
            if sensor_loc == 'L':
                self.leftDistance = data
            elif sensor_loc == 'F':
                self.frontDistance = data
            elif sensor_loc == 'R':
                self.rightDistance = data

    def run(self):
        while True:
            self.update_sensors()
            self.check_and_drive_front()

    def clear_gpios(self):
        print("Clearing GPIO")
        print("All GPIOs CLEARED")


if __name__ == "__main__":
    avoid = ObjectAvoid()
    avoid.run()

