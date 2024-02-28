import tkinter as tk
from tkinter.ttk import * 
import random
from PIL import Image, ImageTk
#import imageio
import subprocess
import cv2
from PIL import Image, ImageTk
import threading



class SARAGUI:
    def __init__(self,master):
        self.master=master
        #title of window 
        self.master.title("S.A.R.A")
        #sets window color to skyblue 
        self.master.config(bg="skyblue")
        #size of window for testing and editing on laptop
        self.master.geometry("800x480") 
        self.starterPage()
        self.video_thread = threading.Thread(target=self.stream_video)
        self.video_thread.start()
    
    

    def starterPage(self):
        #top left frame with Label 
        self.leftFrame=tk.Frame(self.master,width=220, height=150,bg='white')
        self.leftFrame.grid(row=0,column=0,padx=25,pady=5)

        #Place Frame
        #self.leftFrame.place(x=30, y=10)


        #Add Label 
        Label(self.leftFrame,text="S.A.R.A",font=("Arial",40),background='grey').pack()

        #left middle frame with image 
        self.leftMiddleFrame=tk.Frame(self.master,width=220, height=150,bg='red')
        self.leftMiddleFrame.grid(row=1,column=0,padx=25,pady=5)

        #Place Frame
        #self.leftMiddleFrame.place(x=30, y=100)

        try:
            # Load and resize image
            image = Image.open("C:\\Users\\Student\\Documents\\Capstone\\RRR-Capstone-\\GUI\\Images\\image.png")

            resized_image = image.resize((int(image.width /6 ), int(image.height / 6)))

            # Convert to PhotoImage
            self.image_tk = ImageTk.PhotoImage(resized_image)

            # Display the image in a label
            image_label = tk.Label(self.leftMiddleFrame, image=self.image_tk)
            image_label.pack()

        except tk.TclError as e:
            print(f"Error loading image: {e}")



        #Label(self.leftFrame,image=ima).pack()

        # Stats Frame
        self.statsFrame=tk.Frame(self.master,width=220, height=200, bg='grey')
        self.statsFrame.grid(row=1,column=0,padx=10,pady=5)
        #Place Frame for Left Frame 
        self.statsFrame.place(x=15, y=250)

        # Additional labels for Temperature, Longitude, Latitude, and Battery
        temperature_label = tk.Label(self.statsFrame, text="Temperature", bg='grey')
        temperature_label.grid(row=1, column=0, padx=7, pady=5)
        longitude_label = tk.Label(self.statsFrame, text="Longitude", bg='grey')
        longitude_label.grid(row=2, column=0, padx=7, pady=5)
        latitude_label = tk.Label(self.statsFrame, text="Latitude", bg='grey')
        latitude_label.grid(row=3, column=0, padx=7, pady=5)
        battery_label = tk.Label(self.statsFrame, text="Battery", bg='grey')
        battery_label.grid(row=4, column=0, padx=7, pady=5)

                # Additional labels with dynamic values
        temperature_value = tk.Label(self.statsFrame, text=str(random.randint(0, 100)) + "°C", bg='grey')
        temperature_value.grid(row=1, column=1, padx=7, pady=5)
        longitude_value = tk.Label(self.statsFrame, text=str(random.uniform(-180, 180)), bg='grey')
        longitude_value.grid(row=2, column=1, padx=7, pady=5)
        latitude_value = tk.Label(self.statsFrame, text=str(random.uniform(-90, 90)), bg='grey')
        latitude_value.grid(row=3, column=1, padx=7, pady=5)
        battery_value = tk.Label(self.statsFrame, text=str(random.randint(0, 100)) + "%", bg='grey')
        battery_value.grid(row=4, column=1, padx=7, pady=5)

        self.videoFrame = tk.Frame(self.master, width=535, height=300, bg='grey')
        self.videoFrame.place(x=250, y=10)
        self.videoLabel = tk.Label(self.videoFrame)
        self.videoLabel.pack()

        btn_open_second_window = tk.Button(self.master, text="2", command=self.openSecondWindow)
        btn_open_second_window.place(x=20, y=450)

    def openSecondWindow(self):
        subprocess.Popen(["python", "c:\\Users\\Student\\Documents\\Capstone\\RRR-Capstone-\\GUI\\joystickTest.py"])

    def update_video_frame(self):
        if self.current_frame < self.video_length:
            frame = self.video.get_data(self.current_frame)
            image = Image.fromarray(frame)
            resized_image = image.resize((535, 300), Image.ANTIALIAS)  # Corrected line
            tk_image = ImageTk.PhotoImage(resized_image)

            self.videoLabel.config(image=tk_image)
            self.videoLabel.image = tk_image

            self.master.after(30, self.update_video_frame)  # Schedule the next frame update after 30 milliseconds
            self.current_frame += 1

    def stream_video(self):
        video_capture = cv2.VideoCapture(0)
        while True:
            ret, frame = video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                img = img.resize((535, 300), Image.ANTIALIAS)  # Corrected line
                img_tk = ImageTk.PhotoImage(image=img)
                self.videoLabel.config(image=img_tk)
                self.videoLabel.image = img_tk

                # Update other GUI elements (example: dynamic values)
                self.update_dynamic_values()


    def update_dynamic_values(self):
        # Update dynamic values here (example: random values for demonstration)
        self.temperature_value.config(text=str(random.randint(0, 100)) + "°C")
        self.longitude_value.config(text=str(random.uniform(-180, 180)))
        self.latitude_value.config(text=str(random.uniform(-90, 90)))
        self.battery_value.config(text=str(random.randint(0, 100)) + "%")


# Creates Window 
root= tk.Tk()
#run class
SARAGUI(root)
#Initates Run
root.mainloop()