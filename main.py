from tkinter import *
from UI import WriteOrDye, UserWriting, StartButton, Timer

countdown = None


def start_app(event):
    """triggers the start of app"""
    writing.focus()
    start_timer(5)


def start_timer(count):
    global countdown
    if count >= 0:
        timer.config(text=f"{count} secs")
        countdown = window.after(1000, start_timer, count - 1)
    else:
        writing.end_app()


def is_writing(event):
    global countdown
    window.after_cancel(countdown)
    timer.config(text="5 secs")
    start_timer(5)


window = WriteOrDye()
writing = UserWriting()
start = StartButton()
timer = Timer()


start.bind("<Button>", start_app)
writing.bind("<Key>", is_writing)

# keep window open
window.mainloop()
