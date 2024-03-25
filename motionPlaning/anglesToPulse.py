import numpy as np

##Need to adjust the pulse additions with caliberation
## According to servo angle to pulse: 
#500usec ~ 2500usec for 0° ~ 270° (90°--1166usec, 180°--1833usec).

def convert(FR_angles, FL_angles,BR_angles, BL_angles):
#     pulse = np.concatenate((FR_angles, FL_angles,BR_angles, BL_angles))
    pulse = np.empty([12])
    #FR
    pulse[0] = int(7.4074*(FR_angles[0])) + 400
    pulse[1] = int(7.4074*(FR_angles[1])) + 400
    pulse[2] = FR_angles[2]

    #FL
    pulse[3] = int(7.4074*(FL_angles[0])) + 400
    pulse[4] = int(7.4074*(FL_angles[1])) + 400
    pulse[5] = FL_angles[2]

    #BR
    pulse[6] = BR_angles[0]
    pulse[7] = int(7.4074*(BR_angles[1])) + 400
    pulse[8] = int(7.4074*(BR_angles[2])) + 400

    #BL
    pulse[9] = BL_angles[0]
    pulse[10] = int(7.4074*(BL_angles[1])) + 400
    pulse[11] = int(7.4074*(BL_angles[2])) + 400
    
    return pulse