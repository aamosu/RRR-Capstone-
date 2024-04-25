import RPi.GPIO as GPIO
import time
import serial

class RobotControl:
    def __init__(self, port='/dev/ttyACM0', baudrate=9600, timeout=1):
        self.ser = serial.Serial(port, baudrate, timeout=timeout)
        self.threshold = 20
        self.frontDistance = 0
        self.leftDistance = 0
        self.rightDistance = 0

        # GPIO setup
        GPIO.setmode(GPIO.BCM)
        self.sensors = {
            'front': {'trig': 17, 'echo': 27},
            'left': {'trig': 5, 'echo': 6},
            'right': {'trig': 9, 'echo': 11}
        }

        for sensor, pins in self.sensors.items():
            GPIO.setup(pins['trig'], GPIO.OUT)
            GPIO.setup(pins['echo'], GPIO.IN)

    def measure_distance(self, trig, echo):
        GPIO.output(trig, False)
        time.sleep(0.1)
        GPIO.output(trig, True)
        time.sleep(0.00001)
        GPIO.output(trig, False)
        start_time = time.time()

        while GPIO.input(echo) == 0:
            start_time = time.time()
        while GPIO.input(echo) == 1:
            stop_time = time.time()

        elapsed_time = stop_time - start_time
        distance = (elapsed_time * 34300) / 2
        return distance

    def update_sensors(self):
        for sensor, pins in self.sensors.items():
            distance = self.measure_distance(pins['trig'], pins['echo'])
            setattr(self, sensor + 'Distance', distance)
            print(f"{sensor.capitalize()} Distance: {distance:.2f} cm")

    def go_forward(self):
        print("Going Forward!")
        self.ser.write(b'F')
        time.sleep(2)

    def turn_left(self):
        print("Turning Left")
        self.ser.write(b'L')
        time.sleep(2)

    def turn_right(self):
        print("Turning Right")
        self.ser.write(b'R')
        time.sleep(2)

    def go_backward(self):
        print("Going Backward")
        self.ser.write(b'B')
        time.sleep(2)

    def stop_motors(self):
        print("Stopping")
        self.ser.write(b'S')
        time.sleep(2)

    def decision_logic(self):
        self.update_sensors()
        if self.frontDistance < self.threshold:
            self.stop_motors()
            if self.rightDistance < self.threshold and self.leftDistance > self.threshold:
                self.turn_left()
                self.turn_right()
            elif self.leftDistance < self.threshold and self.rightDistance > self.threshold:
                self.turn_right()
                self.turn_left()
            elif self.rightDistance > self.threshold and self.leftDistance > self.threshold:
                self.go_forward()
            else:
                self.go_backward()

        else:
            self.go_forward()

def main():
    robot = RobotControl()
    try:
        while True:
            robot.decision_logic()
            time.sleep(1)  # Adjust timing as needed

    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()
