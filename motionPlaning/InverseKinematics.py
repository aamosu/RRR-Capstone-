import numpy as np

#InverseKinematics.py

#Calculating the joint angles needed to achieve a certain position of the end effector (foot)
#Given a desired position for the foot, compute the necessary angles for each servo in a leg.

#Calculations derived from https://www.mdpi.com/2076-3417/12/9/4358

l, l1, l2 = 1.93, .869, 3.119 #in

def inverse_kinematics(x, y):
    # Calculating distances AC and EC using the given positions of the foot-end point C (x, y)
    l_AC = np.sqrt(x**2 + y**2)
    l_EC = np.sqrt((x - l)**2 + y**2)

    # Using cosine law to find the angles, with inputs clipped to [-1, 1]
    cos_CAE = np.clip((l_AC**2 + l**2 - l_EC**2) / (2 * l * l_AC), -1, 1)
    cos_CEA = np.clip((l_EC**2 + l**2 - l_AC**2) / (2 * l * l_EC), -1, 1)
    cos_BAC = np.clip((l1**2 + l_AC**2 - l2**2) / (2 * l1 * l_AC), -1, 1)
    cos_CED = np.clip((l1**2 + l_EC**2 - l2**2) / (2 * l1 * l_EC), -1, 1)

    # Calculating the angles using np.arccos with clipped inputs
    angle_CAE = np.arccos(cos_CAE)
    angle_CEA = np.arccos(cos_CEA)
    angle_BAC = np.arccos(cos_BAC)
    angle_CED = np.arccos(cos_CED)

    # Calculating theta1 and theta2
    theta1 = np.rad2deg(angle_CAE + angle_BAC)
    theta2 = np.rad2deg(np.pi - angle_CEA - angle_CED)

    return theta1, theta2
