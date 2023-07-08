from tkinter import *

LIGHTPINK = "#FCE9F1"
DARKPINK = "#F1D4E5"
TEAL = "#73BBC9"
BLACK = "#080202"


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
        self.title_label.grid(column=3, row=0, columnspan=3)

        self.explanation = Label()
        self.explanation.config(text="If you stop writing for more than 5 seconds, all your progress will be lost.\n So"
                                     " don't give up!\n", font=("Helvetica", 10), fg=BLACK, bg=DARKPINK, pady=20)
        self.explanation.grid(column=3, row=1, columnspan=3)

        self.empty_column_1 = Label(text="", bg=DARKPINK, width=10)
        self.empty_column_1.grid(column=0, row=0, rowspan=5)
        self.empty_column_2 = Label(text="", bg=DARKPINK, width=10)
        self.empty_column_2.grid(column=2, row=0, rowspan=5)
        self.empty_column_3 = Label(text="", bg=DARKPINK, width=10)
        self.empty_column_3.grid(column=6, row=0, rowspan=5)


class UserWriting(Text):
    """creates a TextBox on the User Interface"""
    def __init__(self):
        super().__init__()
        self.config(width=51, height=5, font=("Helvetica", 20), bg=LIGHTPINK, pady=20)
        self.grid(column=3, row=2, columnspan=3)

    def end_app(self):
        """deletes the content of the TextBox"""
        self.delete("1.0", END)


class StartButton(Button):
    """creates a Button on the User Interface"""
    def __init__(self):
        super().__init__()
        self.config(text="START", font=("Helvetica", 25, "bold"), bg=TEAL, fg=BLACK)
        self.grid(column=1, row=3)


class Timer(Label):
    """creates a Label on the User Interface"""
    def __init__(self):
        super().__init__()
        self.config(text="5 secs", font=("Helvetica", 30, "bold"), bg=TEAL, fg=BLACK,)
        self.grid(column=7, row=3)
