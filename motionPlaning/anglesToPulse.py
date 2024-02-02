import numpy as np

##Need to adjust the pulse additions with caliberation
## According to servo angle to pulse: 
#500usec ~ 2500usec for 0° ~ 270° (90°--1166usec, 180°--1833usec).

def convert(BR_angles, BL_angles,FR_angles, FL_angles):
    pulse = np.empty([8])
    #BR
    pulse[0] = int(-12.9556 * np.rad2deg(-BR_angles[0])) + 950
    pulse[1] = int(-12.9556 * np.rad2deg(BR_angles[1])) + 2280
    #BL
    pulse[2] = int(12.9556 * np.rad2deg(BL_angles[0])) + 1020 
    pulse[3] = int(12.9556 * np.rad2deg(BL_angles[1])) + 570
    #FR
    pulse[4] = int(12.9556 * np.rad2deg(-FR_angles[0])) + 1060 
    pulse[5] = int(-12.9556 * np.rad2deg(FR_angles[1])) + 2335 
    #FL
    pulse[6] = int(-12.9556 * np.rad2deg(FL_angles[0])) + 890
    pulse[7] = int(12.9556 * np.rad2deg(FL_angles[1])) + 710
    return pulse