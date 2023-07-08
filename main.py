from UI import WriteOrDye, UserWriting, StartButton, Timer
import time
from tkinter import messagebox

countdown = None
start_time = 0
end_time = 0


def start_app(event):
    """focuses the cursor to the TextBox and calls function start_timer"""
    global start_time
    writing.focus()
    start_timer(5)
    start_time = time.time()


def start_timer(count):
    """starts timer with the set amount 'count', while timer is running, refreshes window every second to create
    impression of a running countdown, when count is 0, calls function end_app"""
    global countdown
    if count >= 0:
        timer.config(text=f"{count} secs")
        countdown = window.after(1000, start_timer, count - 1)
    else:
        writing.end_app()
        calculate_time()


def is_writing(event):
    """cancels the running countdown, resets the timer by resetting the displayed text, calls function start_timer"""
    global countdown
    window.after_cancel(countdown)
    timer.config(text="5 secs")
    start_timer(5)


def calculate_time():
    """calculates time between call of start_app and end_app, creates pop-up window that shows runtime, resets start
    and end time"""
    global start_time, end_time
    end_time = time.time()
    run_time = round((end_time - start_time)/60)
    messagebox.showinfo(title="Well done!", message=f"You were writing for {run_time} min")
    start_time = 0
    end_time = 0


window = WriteOrDye()
writing = UserWriting()
start = StartButton()
timer = Timer()


start.bind("<Button>", start_app)
writing.bind("<Key>", is_writing)

# keep window open
window.mainloop()
