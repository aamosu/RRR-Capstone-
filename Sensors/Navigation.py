import serial
import time
import math

# Initialize serial connections to Arduino boards
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    )

#Coordinates below need to be manually entered by user once Rocket location is known
latitude2 = 38.899722
longitude2 = -77.047712

line = None

# Convert degrees to radians
def dtor(fdegrees):
    return fdegrees * math.pi / 180

# Convert radians to degrees
def rtod(fradians):
    return fradians * 180.0 / math.pi
    
# Calculate Distance Between Coordinates
def calc_distance(lat1, lon1, lat2, lon2):
    dlon = dtor(lon2 - lon1)
    dlat = dtor(lat2 - lat1)
    a = math.pow(math.sin(dlat/2), 2) + math.cos(dtor(lat1)) * math.cos(dtor(lat2)) * math.pow(math.sin(dlon/2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    dist = 20925656.2 * c  # Radius of the earth (6378140 meters) in feet 20925656.2
    return int(dist + 0.5)
    
# Get bearing between coordinates
def calc_bearing(lat1, lon1, lat2, lon2):
    lat1 = dtor(lat1)
    lon1 = dtor(lon1)
    lat2 = dtor(lat2)
    lon2 = dtor(lon2)

    # Determine angle
    bearing = math.atan2(math.sin(lon2-lon1)*math.cos(lat2), (math.cos(lat1)*math.sin(lat2))-(math.sin(lat1)*math.cos(lat2)*math.cos(lon2-lon1)))
    # Convert to degrees
    bearing = rtod(bearing)
    # Use mod to turn -90 = 270
    bearing = (bearing + 360.0) % 360
    return int(bearing + 0.5)  # Bearing returned is read as 0 degrees = North, 90 degrees = East etc.

# Function to read GPS location
def read_gps_location(line):
    # Parse GPS data and return latitude, longitude
    latitude1 = float(line[1])
    longitude1 = float(line[2])
    return latitude1, longitude1

# Function to read current heading from the compass
def read_compass_heading(line):  
    heading = float(line[0])
    return heading

# Function to check if the robot is correctly aligned with the required heading
def is_correctly_aligned(current_heading, required_heading, tolerance=5):
    # Check if the absolute difference between current heading and required heading is within tolerance
    if (abs(current_heading - required_heading) <= 30) or (abs(current_heading - required_heading) >= 330):
        return True
    else:
        return False

# Main function
def main():
    try:
        while True:
            line = ser.readline().decode().strip().split(',')
            if (len(line) == 3):
                # Read GPS location
                latitude1, longitude1 = read_gps_location(line)
                
                # Read distance and bearing to the rocket
                distance = calc_distance(latitude1, longitude1, latitude2, longitude2)
                bearing = calc_bearing(latitude1, longitude1, latitude2, longitude2)
                
                # Read current heading from the compass
                current_heading = read_compass_heading(line)
                
                # Calculate required heading to reach the rocket
                required_heading = (bearing + 360) % 360  # Ensure heading is within [0, 360) range
                
                # Check if the robot is correctly aligned with the required heading
                aligned = is_correctly_aligned(current_heading, required_heading)
                
                # Print information
                print("Current Location (Lat, Long):", latitude1, longitude1)
                print("Distance to Rocket:", distance, "meters")
                print("Required Heading to Reach Rocket:", required_heading, "degrees")
                print("Current Heading of the Robot:", current_heading, "degrees")
                print("Is the Robot Correctly Aligned?:", aligned)
                print("------------------------------------")
                
                time.sleep(1)  # Adjust sleep time according to your requirement

    except KeyboardInterrupt:
        # Handle keyboard interrupt
        print("Program terminated by user.")
    finally:
        # Close serial connections
        ser.close()

if __name__ == "__main__":
    main()
