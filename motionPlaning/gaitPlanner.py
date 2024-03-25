#gaitPlanner.py

#Generating the sequences of foot positions over time to create walking patterns (gaits). 
#This module would plan the path that the foot needs to take for the robot to walk
# walk, trot, stop

import numpy as np

def arcTrajectory(x_s, step_length, step_height,step_offset, num_points=4):
    """
    Generates the points for half of the cycloid trajectory of the foot for the swing phase.
    
    Parameters:
    - x_s: Starting x coordinate of the foot-end.
    - step_length: The distance between the starting and landing points.
    - step_height: The maximum height of the foot-end from the ground.
    - num_points: Number of points to generate for the trajectory.
    
    Returns:
    - x, y: The coordinates of the foot-end points in the half-cycloid trajectory.
    """
    t = np.linspace(np.pi, 0, num_points)  # Only go from 0 to pi for half the cycloid
    x = x_s + (step_length / 2) * (1 - np.cos(t))
    y = step_height * (1 - np.sin(t))
    
    y = np.append(y, np.linspace(y[-1],y[0],int(num_points/2))[1:])
    x = np.append(x, np.linspace(x[-1],x[0],int(num_points/2))[1:]) -x[-1]
    return x, -(-(y+step_offset)+step_height)


