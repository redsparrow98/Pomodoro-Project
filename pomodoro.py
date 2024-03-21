from tkinter import *
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    # cancels and stops the timer countdown first
    window.after_cancel(timer)
	# resets the timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # resets the timer_label "Timer"
    timer_label.config(text="Timer", font=(FONT_NAME, 30))
    # reset checkmates to no marks
    check_marks.config(text="")
    # reset the reps to 0 as well
    global reps
    reps = 0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """calls the count down function to start the timer when Start button is pressed"""
    # increases the rep by 1 every time its called
    global reps
    reps += 1
    # determine the length of each section
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # if its the 8th rep then its the long break
        # we can tell if its cleanly divided with no remainders
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        # if its the 2/4/6 rep then its the long break
        # we can tell if its cleanly divided by 2 since it would be even
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        # otherwise its the work time timer
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    """starts the timer from the given input int and updates the
        canvas timer_text to show the countdown on screen stops after it reaches 0"""
    # find the min and seconds(math.floor option flor the number to the closest one so 4.8
    # would still be 4 until it becomes 5.0 etc)
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # if count seconds are 0 then it shows on the screen as 00
    if count_sec == 0:
        count_sec = "00"
    # if there are less than 10s then it shows as 09,08,07 etc
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    #we update the timer text on the screen on the tomato
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        # if timer left is greater than 0 we execute an update on the window
        # every second or 1000ms and we call the count_down function on itself
        # so it would keep going. count - 1 is the positional argument we put
        # in the function that is called and we update the count by reducing it
        # by 1 that iw equal to 1s
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

# window set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# canvas tomato image set up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", \
    font=(FONT_NAME, 32, "bold"))
canvas.grid(column=1, row=1)


# timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1,row=0)

# Start button
start_but = Button(text="Start", font=(FONT_NAME, 10), highlightthickness=0, \
    command=start_timer)
start_but.grid(column=0,row=2)

# reset button
reset_but = Button(text="Reset", font=(FONT_NAME, 10), highlightthickness=0, \
    command=reset_timer)
reset_but.grid(column=2,row=2)

# check marks
check_marks = Label(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)


window.mainloop()