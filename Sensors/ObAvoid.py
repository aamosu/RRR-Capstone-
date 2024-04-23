import time
import serial
import struct 

ser = serial.Serial(
port='/COM4',
baudrate=9600,
parity=serial.PARITY_ODD,
stopbits=serial.STOPBITS_TWO,
bytesize=serial.SEVENBITS
)

threshhold = 20
frontDistance=0
leftDistance=0
rightDistance=0

# Functions for driving
def goforward():
    print ("Going Forward!")
    ser.write("F")
    time.sleep(2)


def turnleft():
    print ("Turning Left")
    ser.write("L")
    time.sleep(2)


def turnright():
    print ("Turning Right")
    ser.write("R")
    time.sleep(2)

def gobackward():
    print ("Going Backward")
    ser.write("B")
    time.sleep(2)

def stopmotors():
    print ("Stopping")
    ser.write("S")
    time.sleep(2)

# Check for obstacles as you drive forward
def checkanddrivefront():
    while frontDistance < threshhold:
        stopmotors()
        if rightDistance < threshhold and leftDistance > threshhold:
            turnleft()
            checkandturnright()
        elif leftDistance < threshhold and rightDistance > threshhold:
            turnright()
            checkandturnleft()
        elif rightDistance > threshhold and leftDistance > threshhold:
            turnright()
            checkandturnleft()
        else:
            gobackward()
            if rightDistance > threshhold:
                turnright()
                checkandturnleft()
            elif leftDistance > threshhold:
                turnleft()
                checkandturnright()
    goforward()

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

