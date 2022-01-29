from tkinter import Button, Label, PhotoImage, Tk, Canvas


# CONSTANTS
OFF_WHITE = "#f1faee"
BLUE = "#457b9d"
DARK_BLUE = "#1d3557"
BROWN = "#ddb892"
FONT_NAME = "Courier"
WORK_MIN = 25/25
SHORT_BREAK_MIN = 5/5
LONG_BREAK_MIN = 20
cycle = 0
conti_aft_zero = True


# Reset timer
def reset_timer():
    global conti_aft_zero
    conti_aft_zero = False
    
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    
    global cycle
    cycle = 0


# Creating window
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg = OFF_WHITE)


# Timer
def timer(count):
    if not conti_aft_zero:
        count = 0
    canvas.itemconfig(timer_text, text=f"{int(count/60):02}:{int(count) % 60:02}")
    if count > 0:
        window.after(1000, timer, count-1)    
    
    elif conti_aft_zero:
        start_timer()


def start_timer():
    global cycle
    global conti_aft_zero
    conti_aft_zero = True
    
    if cycle % 2 == 0:
        check_mark.config(text="✔"*int(cycle/2))
    
    cycle += 1
    
    if cycle % 2 != 0:
        timer_label.config(text="Work", fg=BROWN)
        timer(WORK_MIN * 60)
    
    elif cycle % 8 == 0:
        timer_label.config(text="Long Break", fg=BROWN)
        timer(LONG_BREAK_MIN * 60)
    
    else:
        timer_label.config(text="Break", fg=BROWN)
        timer(SHORT_BREAK_MIN * 60)
    
         

# Time label
timer_label = Label(text="Timer", font=(FONT_NAME, 20, "bold"), fg=DARK_BLUE, bg=OFF_WHITE)
timer_label.grid(column=2, row=0)


# Our canvas with the tomato image and an OFF_WHITE color
canvas = Canvas(width=300, height=300, bg= OFF_WHITE, highlightthickness=0)
tomato = PhotoImage(file="./day28/pomodoro-start/tomato.png")
canvas.create_image(150, 150, image=tomato)
timer_text = canvas.create_text(150, 175, text="00:00", fill="white", font=(FONT_NAME,20, "bold"))
canvas.grid(column=2, row=1)


# Check_mark label
check_mark = Label(font=(FONT_NAME, 10, "bold"), fg=DARK_BLUE, bg=OFF_WHITE)
check_mark.grid(column=2, row=2)


# Start and reset button
start_button = Button(text="Start", fg=BLUE, bg=BROWN, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
reset_button = Button(text="Reset", fg=BLUE, bg=BROWN, highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=3)


window.mainloop()


