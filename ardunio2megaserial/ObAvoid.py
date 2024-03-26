import RPi.GPIO as GPIO
import time
import serial

ser = serial.Serial(
    port='/COM4',
    baudrate=9600,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

while(True):
    line = ser.readline().rstrip()
    if not line:
        continue
    sensorLoc = line[0]
    data = int(line[1:])
    if resultType == 'L':
        leftDistance = data
    elif resultType == 'F':
        frontDistance = data
    elif resultType == 'R':
        rightDistance = data
    else:
        pass


ser.close()
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

threshhold = 20

# GPIO for front ultrasonic
GPIO_TRIGGER_CENTRAL = 9
GPIO_ECHO_CENTRAL = 8
GPIO.setup(GPIO_TRIGGER_CENTRAL, GPIO.OUT)
GPIO.setup(GPIO_ECHO_CENTRAL, GPIO.IN)    

# GPIO for right ultrasonic
GPIO_TRIGGER_RIGHT = 5
GPIO_ECHO_RIGHT = 4
GPIO.setup(GPIO_TRIGGER_RIGHT, GPIO.OUT)
GPIO.setup(GPIO_ECHO_RIGHT, GPIO.IN) 

# GPIO for left ultrasonic
GPIO_TRIGGER_LEFT = 13
GPIO_ECHO_LEFT = 12
GPIO.setup(GPIO_TRIGGER_LEFT, GPIO.OUT)  
GPIO.setup(GPIO_ECHO_LEFT, GPIO.IN)      


# Functions for driving
def goforward():
    print "Going Forward!"


def turnleft():
    print "Turning Left"


def turnright():
    print "Turning Right"


def gobackward():
    print "Going Backward"


def stopmotors():
    print "Stopping"



# Check front obstacle and turn right if there is an obstacle
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
def checkandturnright():
    while rightDistance > threshhold:
        stopmotors()
        turnright()
    goforward()


# Check left obstacle and turn right if there is an obstacle
def checkandturnleft():
    while leftDistance > threshhold:
        stopmotors()
        turnleft()
    goforward()


# Avoid obstacles and drive forward
def obstacleavoiddrive():
    goforward()
    start = time.time()
    while True:
        if frontDistance < threshhold:
            stopmotors()
            checkanddrivefront()      
    cleargpios() #stops motors


def cleargpios():
    print "clearing GPIO"
    # GPIO.output(8, False)
    # GPIO.output(9, False)
    # GPIO.output(13, False)
    # GPIO.output(12, False)
    # GPIO.output(5, False)
    # GPIO.output(4, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)
    # GPIO.output(TBD, False)     
    print "All GPIOs CLEARED"


def main():
    # First clear GPIOs
    cleargpios()
    print "start driving: "
    # Start obstacle avoid driving
    obstacleavoiddrive()

if __name__ == "__main__":
    main()