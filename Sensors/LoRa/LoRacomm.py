#Receiver code starts here
import time
import serial
import struct 



class loRaComm:


    def __init__(self , port):
            #ls -l /dev | grep ACM to identify serial port of the arduino
            self.lora = serial.Serial('/dev/ttyS0', baudrate=115200,timeout=1)
            self.lora.setDTR(False)
            time.sleep(1)
            self.lora.flushInput()
            self.lora.setDTR(True)
            time.sleep(2)
            self.lastTime = 0.
            self.previousMillis = 0.
            self.interval = 0.02 
    def read(self):
            if self.lora.inWaiting() > 0:
                        #print ('here')
                    received_data = self.lora.read(8)  
                    buff=received_data  
                    data= struct.unpack('s',buff)         
                    time.sleep(2)
            return data

    def writeGS(self,data):
        comando = "<{0}#{1}#{2}>" #Input
        command=struct.pack('s',comando.format(str(data[0]),str(data[1]),str(data[2])))
        print(self.lora.write(command))
    
    def writeRobot(self,data):
        comando = "<{0}#{1}#{2}>" #Input
        command=struct.pack('s',comando.format(str(data[0]),str(data[1]),str(data[2])))
        print(self.lora.write(command))
                    