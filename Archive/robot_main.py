import numpy as np
import time
import csv
import serial

from motionPlaning.serialCOM import ArduinoSerial
from motionPlaning import anglesToPulse
import motionPlaning.gaitPlanner as gp
import motionPlaning.InverseKinematics as IK

arduino = ArduinoSerial('COM3') #need to specify the serial port

FR_angles = [0,0,0] #1,2,3
FL_angles = [0,0, 0] #4,5,6
BR_angles = [135,0, 0] #7,8,9
BL_angles = [100,0, 0] #10,11,12

#count =0 

# Parameters for the half-cycloid trajectory
step_length = 2  # Step size in mm
x_s = -step_length / 2  # We start at negative half the step length to center the curve around zero
step_height = 1  # Step height in inches
step_offset = 3.5

# Generate the trajectory points
x_cycloid, y_cycloid = gp.arcTrajectory(x_s, step_length, step_height,step_offset)

i = 0

pulsesCommand = anglesToPulse.convert(FR_angles, FL_angles,BR_angles, BL_angles)
print(pulsesCommand)
arduino.serialSend(pulsesCommand)#send serial command to arduino

theta1_arr = []
theta2_arr = []

for x,y in zip(x_cycloid, y_cycloid):
    theta1, theta2 = IK.inverse_kinematics(x, y)
    theta1_arr.append(theta1)
    theta2_arr.append(theta2)
    
for k in range(1000000):
    # Calculate joint angles
#     theta1, theta2= IK.inverse_kinematics(x_cycloid[i], y_cycloid[i])
    #print(f"Theta1: {round(theta1,2)} Theta2: {round(theta2,2)}")
    
    # FR_angles = [0,0,0] #1,2,3
    # FL_angles = [225-theta1_arr[i],135-theta2_arr[i], 0] #4,5,6
    # BR_angles = [135, 225-theta1_arr[i],135-theta2_arr[i]] #7,8,9
    # BL_angles = [100,0, 0] #10,11,12

    FL_angles = [0,0,0] #1,2,3
    FR_angles = [225-theta1_arr[i],135-theta2_arr[i], 0] #4,5,6
    BR_angles = [135,225-theta1_arr[i], 135-theta2_arr[i]] #7,8,9
    BL_angles = [100,0, 0] #10,11,12
    
    #print(len(x_cycloid))
    if i == len(x_cycloid) -1:
        i = 0
        continue
    else:
        i+=1
        #print(i)

    pulsesCommand = anglesToPulse.convert(FR_angles, FL_angles,BR_angles, BL_angles)
    print(pulsesCommand)
    arduino.serialSend(pulsesCommand)#send serial command to arduino
#     count += 1
    time.sleep(1)

