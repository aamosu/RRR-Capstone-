import RPi.GPIO as GPIO
import time
import serial
import struct 

threshhold = 20
frontDistance = 0
leftDistance = 0
rightDistance = 0
Ftrig_pin =
Fecho_pin =
Ltrig_pin =
Lecho_pin =
Rtrig_pin =
Recho_pin =

GPIO.setup(FTRIG_PIN, GPIO.OUT)
GPIO.setup(FECHO_PIN, GPIO.IN)
GPIO.setup(LTRIG_PIN, GPIO.OUT)
GPIO.setup(LECHO_PIN, GPIO.IN)
GPIO.setup(RTRIG_PIN, GPIO.OUT)
GPIO.setup(RECHO_PIN, GPIO.IN)

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
    #Serial write somthing like F


def turnleft():
    print ("Turning Left")
    time.sleep(2)
    #Serial write somthing like L
    print ("Turned")
    time.sleep(2)

def turnright():
    print ("Turning Right")
    #Serial write somthing like R
    time.sleep(2)
    print("Turned")

def gobackward():
    print ("Going Backward")
    time.sleep(2)
    #Serial write somthing like B

def stopmotors():
    print ("Stopping")
    time.sleep(2)
    #Serial write somthing like S
    
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

def get_distance(TRIG_PIN, ECHO_PIN):
    GPIO.output(TRIG_Pin, True)
    time.sleep(.00001)
    GPIO.output(TRIG_PIN, False)
    start_time = time.time()
    stop_time = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()
    pulse_duration = stop_time - start_time
    distance = pulse_duration * 17150  # Speed of sound is 34300 cm/s, so divide by 2 to get one-way distance
    distance = round(distance)
    return distance
    
def checkSensors():
    frontDistance = get_distance(Ftrig_pin, Fecho_pin)
    leftDistance = get_distance(Ltrig_pin, Lecho_pin)
    rightDistance = get_distance(Rtrig_pin, Recho_pin)

    #Serial write the values of all distance values here

    return frontDistance, leftDistance, rightDistance

def main():
    goforward()
    while True:
        frontDistance, leftDistance, rightDistance = checkSensors(ser)
        time.sleep(3)
        obstacleavoiddrive()
    
if __name__=="__main__":
    main()

