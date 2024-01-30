import numpy as np
import time
import csv
import serial

from motionPlaning.serialCom import ArduinoSerial
from motionPlaning import anglesToPulse
import motionPlaning.gaitPlanner as gp
import motionPlaning.InverseKinematics as IK


arduino = ArduinoSerial('/dev/ttyACM0') #need to specify the serial port

# Define link lengths and foot position (replace with actual values)
#L1 = horizontal distance between servos
#L2 and L5 = Metal Horn length
#L3 = Leg Length
L1, L2, L3, L5 = 56, 25, 90, 25 #mm

BR_angles = [0,0] #1,2
BL_angles = [0,0] #3,4
FR_angles = [0,0] #5,6
FL_angles = [0,0] #7,8

x_traj,y_traj = gp.arcTrajectory(100, 10)
i = 0

pulsesCommand = anglesToPulse.convert(BR_angles, BL_angles,FR_angles, FL_angles)
#print(pulsesCommand)
arduino.serialSend(pulsesCommand)#send serial command to arduino

while(True):

    # Calculate joint angles
    theta1 = IK.calculate_theta1(x_traj[i], y_traj[i], L1, L2, L3)
    theta2 = IK.calculate_theta2(x_traj[i], y_traj[i], L1, L5)

    BR_angles = [theta1,theta2] #1,2
    BL_angles = [theta1-np.radians(90),theta2-np.radians(90)] #3,4
    FR_angles = [theta1-np.radians(90),theta2-np.radians(90)] #5,6
    FL_angles = [theta1,theta2] #7,8
    
    if i >= len(x_traj):
        i = 0
    else:
        i+=1

    pulsesCommand = anglesToPulse.convert(BR_angles, BL_angles,FR_angles, FL_angles)
    #print(pulsesCommand)
    arduino.serialSend(pulsesCommand)#send serial command to arduino

