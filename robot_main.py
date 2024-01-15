import numpy as np
import time
import csv

from motionPlaning.serialCOM import ArduinoSerial
from motionPlaning import anglesToPulse

arduino = ArduinoSerial('/dev/ttyACM0') #need to specify the serial port


#R_angles, FL_angles, BR_angles, BL_angles , transformedBodytoFeet = robotKinematics.solve(orn + commandOrn, pos + commandPose , bodytoFeet)

BR_angles = [0,0] #1,2
BL_angles = [0,0] #3,4
FR_angles = [0,0] #5,6
FL_angles = [0,0] #7,8

pulsesCommand = anglesToPulse.convert(BR_angles, BL_angles,FR_angles, FL_angles)
arduino.serialSend(pulsesCommand)#send serial command to arduino

