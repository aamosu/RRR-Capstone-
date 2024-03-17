import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import cv2
import threading
import subprocess
import numpy as np
import serial 


class SARAGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("S.A.R.A")
        self.master.config(bg="skyblue")
        self.master.geometry("800x480") 
        self.starterPage()
        self.video_thread = threading.Thread(target=self.stream_video)
        self.video_thread.start()
        #self.update_dynamic_values()
        self.ser = serial.Serial("/dev/ttyS0", baudrate=9600)  # Initialize serial port
    
    def starterPage(self):
        self.leftFrame = tk.Frame(self.master, width=220, height=150, bg='white')
        self.leftFrame.grid(row=0, column=0, padx=25, pady=5)
        Label(self.leftFrame, text="S.A.R.A", font=("Arial", 40), background='grey').pack()

        self.leftMiddleFrame = tk.Frame(self.master, width=220, height=150, bg='red')
        self.leftMiddleFrame.grid(row=1, column=0, padx=25, pady=5)

        try:
            image = Image.open("/home/recovery-robot/Desktop/RRR-Capstone-/GUI/Images/Image.png")
            resized_image = image.resize((int(image.width / 4), int(image.height / 4)))
            self.image_tk = ImageTk.PhotoImage(resized_image)
            image_label = tk.Label(self.leftMiddleFrame, image=self.image_tk)
            image_label.pack()
        except tk.TclError as e:
            print(f"Error loading image: {e}")

        self.statsFrame = tk.Frame(self.master, width=220, height=200, bg='grey')
        self.statsFrame.grid(row=5, column=0, padx=10, pady=5)
        self.statsFrame.place(x=15, y=320)

        self.coordinates_label = tk.Label(self.statsFrame, text="Coordinates", bg='grey')
        self.coordinates_label.grid(row=4, column=0, padx=7, pady=5)
        self.coordinates_entry = tk.Text(self.statsFrame, height=2, width=20)
        self.coordinates_entry.grid(row=4, column=1, padx=7, pady=5)
        
        
        self.videoFrame = tk.Frame(self.master, width=535, height=300, bg='grey')
        self.videoFrame.place(x=250, y=10)
        self.videoLabel = tk.Label(self.videoFrame)
        self.videoLabel.pack()
        
        btn_open_second_window = tk.Button(self.master, text=" ", command=self.openSecondWindow)
        btn_open_second_window.place(x=20, y=450)
        
        btn_send_cord = tk.Button(self.master, text="Send", command=self.send_coordinates)
        btn_send_cord.place(x=100, y=450)

    #def update_dynamic_values(self):
        #self.longitude_value.config(text=str(random.uniform(-180, 180)))
        #self.latitude_value.config(text=str(random.uniform(-90, 90)))


    def stream_video(self):
        video_capture = cv2.VideoCapture(0)
        # Load pre-trained MobileNet SSD model
        net = cv2.dnn.readNetFromCaffe("/home/recovery-robot/Desktop/RRR-Capstone-/GUI/MobileNetSSD_deploy.prototxt.txt", "/home/recovery-robot/Desktop/RRR-Capstone-/GUI/MobileNetSSD_deploy.caffemodel")
        while True:
            ret, frame = video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
                net.setInput(blob)
                detections = net.forward()

                # Process detections
                for i in range(detections.shape[2]):
                    confidence = detections[0, 0, i, 2]
                    if confidence > 0.2:  # Filter weak detections
                        box = detections[0, 0, i, 3:7] * np.array([frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]])
                        (startX, startY, endX, endY) = box.astype("int")
                        cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
                img = Image.fromarray(frame)
                img = img.resize((535, 300), Image.ANTIALIAS)
                img_tk = ImageTk.PhotoImage(image=img)

                self.videoLabel.config(image=img_tk)
                self.videoLabel.image = img_tk

    def send_coordinates(self):

        coordinates= self.coordinates_entry.get("1.0", "end-1c")  # Get text from Text widget
        coordinatesNL="C"+coordinates+ "\n"
        self.ser.write(coordinatesNL.encode('utf-8'))

    def openSecondWindow(self):
        subprocess.Popen(["python", "/home/recovery-robot/Desktop/RRR-Capstone-/GUI/joystickTest.py"])

# Creates Window 
root = tk.Tk()
# Run class
SARAGUI(root)
# Initiate Run
root.mainloop()
