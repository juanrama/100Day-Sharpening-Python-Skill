from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global resps
    global timer
    window.after_cancel(timer)
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    check_mark.config(text="")
    resps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global resps
    if resps % 2 != 0:
        label.config(text="Work", fg=GREEN)
        count_down(20)
        resps += 1
    elif resps % 2 == 0 and resps != 8:
        label.config(text="Break", fg=PINK)
        count_down(10)
        resps += 1
    elif resps == 8:
        label.config(text="Break", fg=RED)
        count_down(5)
        resps = 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global resps
    global timer
    timer_num = time.strftime("%M:%S", time.gmtime(count))
    canvas.itemconfig(timer_text, text = timer_num)
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        mark = ""
        work_session = math.floor(resps/2)
        for _ in range(work_session):
            mark += "✓"
        check_mark.config(text=mark)
        start_timer()
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")

canvas = Canvas(width=200, height =224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="White")
canvas.grid(column=1, row=1)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg= GREEN, bg=YELLOW)
label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

stop_button = Button(text="Reset", highlightthickness=0, command=reset)
stop_button.grid(column=2, row=2)

check_mark = Label(font=(FONT_NAME, 15, "bold"), fg= GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()