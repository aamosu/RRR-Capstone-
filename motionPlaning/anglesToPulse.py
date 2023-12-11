import numpy as np

##Need to adjust the pulse additions with caliberation

def convert(FR_angles, FL_angles, BR_angles, BL_angles):
    pulse = np.empty([8])
    #FR
    pulse[0] = int(-10.822 * np.rad2deg(-FR_angles[0])) + 950
    pulse[1] = int(-10.822 * np.rad2deg(FR_angles[1])) + 2280
    #FL
    pulse[2] = int(10.822 * np.rad2deg(FL_angles[0])) + 1020 
    pulse[3] = int(10.822 * np.rad2deg(FL_angles[1])) + 570
    #BR
    pulse[4] = int(10.822 * np.rad2deg(-BR_angles[0])) + 1060 
    pulse[5] = int(-10.822 * np.rad2deg(BR_angles[1])) + 2335 
    #BL
    pulse[6] = int(-10.822 * np.rad2deg(BL_angles[0])) + 890
    pulse[7] = int(10.822 * np.rad2deg(BL_angles[1])) + 710
    return pulse