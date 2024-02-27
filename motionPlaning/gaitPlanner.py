#gaitPlanner.py

#Generating the sequences of foot positions over time to create walking patterns (gaits). 
#This module would plan the path that the foot needs to take for the robot to walk
# walk, trot, stop

import numpy as np
import matplotlib as plt

def arcTrajectory(radius, num_points):
    theta = np.linspace(np.radians(225), np.radians(315), num_points)
    x_bottom = radius * np.cos(theta)
    y_bottom = radius * np.sin(theta)
    
    x_top = x_bottom
    y_top = -y_bottom + (y_bottom[0]*2)
    
    x_combined = np.concatenate([x_bottom,x_top])
    y_combined = np.concatenate([y_bottom,y_top])

    
    return x_combined,y_combined