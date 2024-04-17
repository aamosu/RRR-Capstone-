import serial
import struct 
import time

class LoRaComm:
    def __init__(self, port):
        self.lora = serial.Serial(port, baudrate=9600, timeout=1)

    def readline(self):
        return self.lora.readline()

    def read(self):
        if self.lora.inWaiting() > 0:
            received_data = self.lora.read()  
            buff = received_data  
            data = struct.unpack('s', buff)         
            time.sleep(2)
            return data
        else: 
            return None

    def writeGS(self, data):
        comando = "<{0}#{1}#{2}>" #Input
        command = struct.pack('s', comando.format(str(data[0]), str(data[1]), str(data[2])))
        print(self.lora.write(command))
    
    def writeRobot(self, data):
        comando = "<{0}#{1}#{2}>" #Input
        command = struct.pack('s', comando.format(str(data[0]), str(data[1]), str(data[2])))
        print(self.lora.write(command))
                    
