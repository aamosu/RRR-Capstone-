import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function to update the animation
def update(frame):
    global x, y
    
    # Calculate the distance between current position and target position
    dx = target_x - x
    dy = target_y - y
    distance = np.sqrt(dx**2 + dy**2)
    
    # If the distance is greater than a threshold, move the point towards the target
    if distance > 0.01:
        x += 0.1 * dx / distance
        y += 0.1 * dy / distance
    
    # Update the position of the point
    point.set_data(x, y)
    return point,

# Target coordinate
target_x = 5
target_y = 5

# Initial position of the moving point
x = 0
y = 0

# Create a figure and axis
fig, ax = plt.subplots()
ax.set_xlim(-1, 10)
ax.set_ylim(-1, 10)

# Create a point representing the moving coordinate
point, = ax.plot(x, y, marker='o', color='r')

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, 100), interval=100)

plt.title('Animation of a Point Moving Towards a Target Coordinate')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
