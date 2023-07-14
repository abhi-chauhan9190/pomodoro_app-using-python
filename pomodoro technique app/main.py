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
check="✔"
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps=0
    title_label.config(text='Timer')
    canvas.itemconfig(timer_text,text='00:00')
    title_label2.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_sec=SHORT_BREAK_MIN*60
    long_sec=LONG_BREAK_MIN*60
    if reps%2!=0:
        title_label.config(text=' WORK !')
        count_down(work_sec)

    elif reps%8==0:
        title_label.config(text='BREAK !')
        count_down[long_sec]
    else:
        title_label.config(text='BREAK !')
        count_down(short_sec)        
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec <=9 :
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if(count > 0):
        global timer
        timer=window.after(1000,count_down,count-1)

    else:
        start_timer()  
        mark=""
        for _ in range(math.floor(reps/2)):
            mark+=check
            title_label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro App")
window.minsize(width=400,height=450)
window.config(padx=80,pady=50,bg=YELLOW )
canvas=Canvas(width=200,height=224,bg=YELLOW , highlightthickness=0)
imgg=PhotoImage(file='pomodoro technique app/tomato.png')
canvas.create_image(100,112,image=imgg)
timer_text=canvas.create_text(103,131,text="00:00",fill="white",font=(FONT_NAME, 35,'bold'))
canvas.grid(column=5,row=2)

title_label=Label(text="Timer",font=(FONT_NAME,30,'bold'),fg=GREEN,bg=YELLOW)
title_label.grid(column=5,row=0)
title_label.config(padx=30)

title_label2=Label(fg=GREEN ,font=(FONT_NAME,20,'bold'),bg=YELLOW)
title_label2.grid(column=5,row=6)

buttons=Button(text='Start',bg=PINK,font=(FONT_NAME,20,'bold'),highlightthickness=0 , command=start_timer)
buttons.grid(column=3,row=5)

buttonr=Button(text='RESET',bg=RED,font=(FONT_NAME,20,'bold'),highlightthickness=0,command=reset_timer)
buttonr.grid(column=6,row=5)

window.mainloop()