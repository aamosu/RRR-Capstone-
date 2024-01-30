import tkinter as tk
from tkinter.ttk import * 

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
            #load image 
            image = tk.PhotoImage(file="robot image.png")
            imageResize=image.subsample(6,6)
            image_label = tk.Label(self.leftMiddleFrame,image=imageResize)
            image_label.pack()
        except tk.TclError as e:
            print(f"Error loading image: {e}")


        #Label(self.leftFrame,image=ima).pack()

        # Stats Frame
        self.statsFrame=tk.Frame(self.master,width=220, height=200, bg='grey')
        self.statsFrame.grid(row=1,column=0,padx=10,pady=5)
        #Place Frame for Left Frame 
        self.statsFrame.place(x=15, y=250)

        #Video Frame
        #Right Frame Size, Charc 
        self.videoFrame=tk.Frame(self.master,width=535, height=300, bg='grey')
        #self.videoFrame.grid(row=0,column=1,padx=10,pady=5)

        #Place Frame Video Frame 
        self.videoFrame.place(x=250, y=10)

        #Diagonistic Frame 
        #Right Frame Size, Charc 
        self.diagonisticFrame=tk.Frame(self.master,width=535, height=130, bg='grey')
        self.diagonisticFrame.grid(row=1,column=1,padx=10,pady=5)

        #Place Frame Video Frame 
        self.diagonisticFrame.place(x=250, y=330)



# Creates Window 
root= tk.Tk()
#run class
SARAGUI(root)
#Initates Run
root.mainloop()
