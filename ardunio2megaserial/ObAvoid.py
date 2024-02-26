#import RPi.GPIO as GPIO
import time
import serial
import struct 

threshhold = 20


# Avoid obstacles and drive forward
def obstacleavoiddrive(frontDistance, leftDistance, rightDistance):
    time.sleep(2)
    goforward()
    start = time.time()
    if frontDistance < threshhold:
            checkanddrivefront(frontDistance, leftDistance, rightDistance)       

# Functions for driving
def goforward():
    print ("Going Forward!")
    time.sleep(10)


def turnleft():
    print ("Turning Left")


def turnright():
    print ("Turning Right")


def gobackward():
    print ("Going Backward")
    time.sleep(3)


def stopmotors():
    print ("Stopping")

# Check front obstacle and turn right if there is an obstacle
def checkanddrivefront(frontDistance, leftDistance, rightDistance):
    time.sleep(5)
    while frontDistance < threshhold:
        stopmotors()
        if rightDistance < threshhold and leftDistance > threshhold:
            turnleft()
            checkandturnright(rightDistance)
        elif leftDistance < threshhold and rightDistance > threshhold:
            turnright()
            checkandturnleft(leftDistance)
        elif rightDistance > threshhold and leftDistance > threshhold:
            turnright()
            checkandturnleft(leftDistance)
        else:
            gobackward()
            if rightDistance > threshhold:
                turnright()
                checkandturnleft(leftDistance)
            elif leftDistance > threshhold:
                turnleft()
                checkandturnright(rightDistance)
    goforward()


# Check right obstacle and turn left if there is an obstacle
def checkandturnright(rightDistance):
    while rightDistance > threshhold:
        stopmotors()
        turnright()
    goforward()


# Check left obstacle and turn right if there is an obstacle
def checkandturnleft(leftDistance):
    while leftDistance > threshhold:
        stopmotors()
        turnleft()
    goforward()


def cleargpios():
    print ("clearing GPIO")    
    print ("All GPIOs CLEARED")
    

def main():
  frontDistance=0
  leftDistance=0
  rightDistance=0
  ser = serial.Serial(
    port='/COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
    )
  while(True):
    print ("start driving: ")
    # Start obstacle avoid driving
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
    obstacleavoiddrive(frontDistance, leftDistance, rightDistance)
    
if __name__=="__main__":
    main()

