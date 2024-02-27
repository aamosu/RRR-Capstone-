import tkinter as tk
from tkinter.ttk import * 
import random
from PIL import Image, ImageTk
#import imageio




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

        #label_widgets.extend([temperature_label, longitude_label, latitude_label, battery_label])


        #Video Frame
        #Right Frame Size, Charc 
        self.videoFrame=tk.Frame(self.master,width=535, height=300, bg='grey')
        #self.videoFrame.grid(row=0,column=1,padx=10,pady=5)

        # Load video frames
        #self.load_video_frames()

        #Place Frame Video Frame 
        self.videoFrame.place(x=250, y=10)


        btn_open_second_window = tk.Button(self.master, text="2", command=self.openSecondWindow)
        btn_open_second_window.place(x=20, y=450)

    def move(self, direction):
        # Implement your robot movement logic here
        print(f"Moving {direction}")

    def openSecondWindow(self):
        second_window = tk.Toplevel(self.master)
        second_window.title("S.A.R.A Controls")
        second_window.geometry("800x480")

        # Adding control frame with arrow buttons
        control_frame = tk.Frame(second_window, width=200, height=150, bg='grey')
        control_frame.grid(row=0, column=0, padx=25, pady=5)
        control_frame.place(x=100, y=50)

        self.create_arrow_buttons(control_frame)

    def load_video_frames(self):
        # Load video frames from a video file
        video_path = "C:\\Users\\Student\\Documents\\Capstone\\testVid.mp4"
        self.video = imageio.get_reader(video_path)
        self.video_length = len(self.video)
        self.current_frame = 0

        self.update_video_frame()

    def update_video_frame(self):
        if self.current_frame < self.video_length:
            frame = self.video.get_data(self.current_frame)
            image = Image.fromarray(frame)
            resized_image = image.resize((535, 300), Image.ANTIALIAS)
            tk_image = ImageTk.PhotoImage(resized_image)

            self.videoLabel.config(image=tk_image)
            self.videoLabel.image = tk_image

            self.master.after(30, self.update_video_frame)  # Schedule the next frame update after 30 milliseconds
            self.current_frame += 1


# Creates Window 
root= tk.Tk()
#run class
SARAGUI(root)
#Initates Run
root.mainloop()