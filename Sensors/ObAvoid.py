import RPi.GPIO as GPIO
import time
import serial
import struct 

threshhold = 20

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
    )

# Avoid obstacles and drive forward
def obstacleavoiddrive():
    frontDistance, leftDistance, rightDistance = checkSensors(ser)
    if frontDistance < threshhold and frontDistance != 0:
        stopmotors()
        if rightDistance < threshhold and (leftDistance > threshhold or leftDistance == 0):
            turnleft() 
            checkandturnright(rightDistance)
        elif leftDistance < threshhold and (rightDistance > threshhold or rightDistance == 0):
            turnright()
            checkandturnleft(leftDistance)
        elif (rightDistance > threshhold or rightDistance == 0) and (leftDistance > threshhold or leftDistance == 0):
            turnright()
            checkandturnleft(leftDistance)
        else:
            while ((rightDistance < threshhold and rightDistance != 0) and (leftDistance < threshhold and rightDistance != 0)):
                gobackward() #once robot finds a side to turn to you cant check side sensors to tell when to turn back as you have backed
                #up far away enough from the initial front obstacle anyways. so we need to explicitly say just walk forward enough before turning
                frontDistance, leftDistance, rightDistance = checkSensors(ser)
                if (rightDistance > threshhold or rightDistance == 0):
                    turnright()
                    checkandturnleft(leftDistance)
                elif (leftDistance > threshhold or leftDistance == 0):
                    turnleft()
                    checkandturnright(rightDistance)
    elif frontDistance > threshhold or frontDistance == 0:
        goforward()


# # GPIO Motor Pins
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)
# GPIO.setup(TBD, GPIO.OUT)  

# Functions for driving
def goforward():
    print ("Going Forward!")
    time.sleep(2)


def turnleft():
    print ("Turning Left")
    time.sleep(2)
    print ("Turned")
    time.sleep(2)

def turnright():
    print ("Turning Right")
    time.sleep(2)
    print("Turned")

def gobackward():
    print ("Going Backward")
    time.sleep(2)

def stopmotors():
    print ("Stopping")
    time.sleep(2)
    
# After turning left to avoid obstacle check when to turn back right on course
def checkandturnright(rightDistance):
    while rightDistance < threshhold:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
        goforward()
    goforward()
    turnright()

# After turning right to avoid obstacle check when to turn back left on course
def checkandturnleft(leftDistance):
    while leftDistance < threshhold:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
        goforward()
    goforward()
    turnleft()

def cleargpios():
    print ("clearing GPIO")
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)     
    print ("All GPIOs CLEARED")
    
def checkSensors(ser):
    lineRead = ser.readline().decode().strip()
    line = lineRead.split()
    print(line)
    frontData = line[0]
    frontDistance = int(frontData[1:])
    leftData = line[1]
    leftDistance = int(leftData[1:])
    rightData = line[2]
    rightDistance = int(rightData[1:])
    return frontDistance, leftDistance, rightDistance

def main():
    goforward()
    while True:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
        time.sleep(3)
        obstacleavoiddrive()
    
if __name__=="__main__":
    main()

