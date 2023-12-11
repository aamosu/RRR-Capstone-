import numpy as np
#InverseKinematics.py

#Calculating the joint angles needed to achieve a certain position of the end effector (foot)
#Given a desired position for the foot, compute the necessary angles for each servo in a leg.

#Calculations derived from https://www.mdpi.com/2076-3417/12/9/4358

def calculate_theta1(Px, Pz, L1, L2, L3):
    # Calculate a and b
    a = (L1 / 2) * L2 - Px * L2 + L2 * L3
    b = Px**2 - 2 * Px * (L1 / 2) - 2 * Px * L3 + Pz**2 + (L1 / 2)**2 + L1 * L3 + L3**2

    # Calculate sθ1 and cθ1
    s_theta1 = ((L1 / 2) - Px + L3) * a / (Pz * b - (L2 / 2) * Pz)
    c_theta1 = a + Pz * np.sqrt(b - L2**2) / b

    # Calculate θ1
    theta1 = np.arctan2(s_theta1, c_theta1)

    return theta1

def calculate_theta2(Px, Pz, L1, L5):
    # Calculate c and d
    c = -4 * Px**2 - 8 * Px * (L1 / 2) - 4 * Pz**2 + L5**2 - 4 * (L1 / 2)**2
    d = Px**2 + 2 * Px * (L1 / 2) + Pz**2 + (L1 / 2)**2
    print(c)
    # Calculate sθ2 and cθ2
    s_theta2 = Pz * (L5 + np.sqrt(d)) / (2 * d)
    c_theta2 = (Px + (L1 / 2)) * (L5 + np.sqrt(c)) / (2 * d)

    # Calculate θ2
    theta2 = np.arctan2(s_theta2, c_theta2)

    return theta2

##Testing the functions
# Define link lengths and foot position (replace with actual values)
L1, L2, L3, L5 = 200, 350, 1000, 350
Px, Pz = 50, 50

# Calculate joint angles
theta1 = calculate_theta1(Px, Pz, L1, L2, L3)
theta2 = calculate_theta2(Px, Pz, L1, L5)

# Print the results
print(f"Theta1: {np.degrees(theta1)} degrees")
print(f"Theta2: {np.degrees(theta2)} degrees")