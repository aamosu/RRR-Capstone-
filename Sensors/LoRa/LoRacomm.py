import time
import serial

class loRaComm:
    def __init__(self, port):
        try:
            # Initialize serial port connection
            self.lora = serial.Serial(port, baudrate=9600, timeout=1)
            self.lora.setDTR(False)  # DTR: Data Terminal Ready control line
            time.sleep(1)            # Wait for the hardware to settle
            self.lora.flushInput()   # Flush startup data
            self.lora.setDTR(True)
            time.sleep(2)            # Wait after setting DTR to True
            self.lastTime = 0.0
            self.previousMillis = 0.0
            self.interval = 0.02     # Sampling rate interval
        except serial.SerialException as e:
            print(f"Error opening serial port {port}: {e}")
            self.lora = None  # Ensure lora is set to None if we fail to open the port

    def read(self):
        if self.lora is not None and self.lora.inWaiting() > 0:
            try:
                received_data = self.lora.read(8)  # Adjust the byte count as needed
                data = received_data.decode('utf-8')  # Decode bytes to string
                time.sleep(2)
                return data
            except serial.SerialException as e:
                print(f"Error reading from serial port: {e}")
        return None

    def writeGS(self, data):
        if self.lora is not None:
            try:
                if isinstance(data, str):
                    command = f"{data}".encode('utf-8')  # Format and encode the string to bytes
                else:
                    command = f"{str(data)}".encode('utf-8')  # Convert to string if not already
                self.lora.write(command)  # Send the command
            except serial.SerialException as e:
                print(f"Error writing to serial port: {e}")

    def writeRobot(self, data):
        if self.lora is not None:
            try:
                if isinstance(data, (list, tuple)) and len(data) == 3:
                    command = f"<{data[0]}#{data[1]}#{data[2]}>".encode('utf-8')
                    self.lora.write(command)  # Send the command
                    print("Command sent successfully")
                else:
                    print("Error: Data must be a list or tuple with exactly three elements.")
            except serial.SerialException as e:
                print(f"Error writing to serial port: {e}")

    def close(self):
        if self.lora is not None:
            self.lora.close()
            print("Serial connection closed")
                    
