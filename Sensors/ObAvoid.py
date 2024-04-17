#import RPi.GPIO as GPIO
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


# Check right obstacle and turn left if there is an obstacle
def checkandturnright(rightDistance):
    while rightDistance < threshhold:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
        goforward()
    goforward()
    turnright()


# Check left obstacle and turn right if there is an obstacle
def checkandturnleft(leftDistance):
    while leftDistance < threshhold:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
    goforward()
    turnleft()


def cleargpios():
    print ("clearing GPIO")    
    print ("All GPIOs CLEARED")

def checkSensors(ser):
    for i in range(3):
        lineRead =ser.readline().rstrip()
        line=lineRead.decode("utf-8")
        print(line)
        if not line:
            continue
        sensorLoc = line[0]
        #print (sensorLoc)
        data = int(line[1:])
            #print(data)
        if sensorLoc == 'L':
            leftDistance = data
        elif sensorLoc == 'F':
            frontDistance = data
        elif sensorLoc == 'R':
            rightDistance = data
        else:
            pass
    

def main():
  print ("start driving: ")
  while(True):
    checkSensors(ser)
    checkanddrivefront()
    
if __name__=="__main__":
    main()

