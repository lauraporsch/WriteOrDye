from tkinter import *
from colors import *


class WriteOrDye(Tk):
    def __init__(self):
        """creates the User Interface for the application"""
        super().__init__()
        self.title("Write Or Dye")
        self.config(bg=DARKPINK)
        width = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry("%dx%d" % (width, height))

        self.title_label = Label()
        self.title_label.config(text="Write Or Dye", font=("Helvetica", 50, "bold"), fg=BLACK, bg=DARKPINK, pady=20)
        self.title_label.grid(column=1, row=0, columnspan=3)

        self.explanation = Label()
        self.explanation.config(text="If you stop writing for more than 5 seconds, all your progress will be lost.\n So"
                                     " don't give up!\n", font=("Helvetica", 10), fg=BLACK, bg=DARKPINK, pady=20)
        self.explanation.grid(column=1, row=1, columnspan=3)


class UserWriting(Text):
    def __init__(self):
        super().__init__()
        self.config(width=51, height=5, font=("Helvetica", 20), bg=LIGHTPINK, pady=20)
        self.grid(column=1, row=2, columnspan=3)

    def end_app(self):
        self.delete("1.0", END)


class StartButton(Button):
    def __init__(self):
        super().__init__()
        self.config(text="START", font=("Helvetica", 25, "bold"), bg=TEAL, fg=BLACK)
        self.grid(column=0, row=3)


class Timer(Label):
    def __init__(self):
        super().__init__()
        self.config(text="5 secs", font=("Helvetica", 30, "bold"), bg=TEAL, fg=BLACK,)
        self.grid(column=4, row=3)


