import serial
import time


class ArduinoSerial:  
    def __init__(self , port):
        #ls -l /dev | grep ACM to identify serial port of the arduino
        self.arduino = serial.Serial(port, 115200, timeout = 1)
        self.arduino.setDTR(False)
        time.sleep(1)
        self.arduino.flushInput()
        self.arduino.setDTR(True)
        time.sleep(2)
        self.lastTime = 0.
        self.previousMillis = 0.
        self.interval = 0.02 #arduino loop running at 20 ms
        
    def serialSend(self, pulse):  
        comando = "<{0}#{1}#{2}#{3}#{4}#{5}#{6}#{7}>" #Input
        command=comando.format(int(pulse[0]), int(pulse[1]), int(pulse[2]), 
                                   int(pulse[3]), int(pulse[4]), int(pulse[5]), 
                                   int(pulse[6]), int(pulse[7]))
        self.arduino.write(bytes(command , encoding='utf8'))
        self.lastTime = time.time()
            
    def close(self):
        self.arduino.close()