import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Multiple Pages Example")
        self.geometry("400x300")  # Set the initial window size

        self.frames = {}

        # Create multiple frames and add them to the frames dictionary
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Define a generic Page class
class Page(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # Common elements for all pages can be added here

# Define individual pages
class StartPage(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)
        label = tk.Label(self, text="Start Page")
        label.pack(pady=10, padx=10)

        # Add elements specific to the Start Page

        button = tk.Button(self, text="Go to Page One", command=lambda: parent.show_frame(PageOne))
        button.pack()

class PageOne(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)
        label = tk.Label(self, text="Page One")
        label.pack(pady=10, padx=10)

        # Add elements specific to Page One

        button = tk.Button(self, text="Go to Start Page", command=lambda: parent.show_frame(StartPage))
        button.pack()

class PageTwo(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)
        label = tk.Label(self, text="Page Two")
        label.pack(pady=10, padx=10)

        # Add elements specific to Page Two

        button = tk.Button(self, text="Go to Start Page", command=lambda: parent.show_frame(StartPage))
        button.pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
