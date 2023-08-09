from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title("DIGITAL CLOCK")

def clock():
    Time_str = strftime('%I:%M:%S %p')
    Time.config(text=Time_str)

    date_str=strftime("%B %d, %Y")
    Date.config(text=date_str)

    day_str=strftime("%A")
    Day.config(text=day_str)

    Time.after(1000,clock)

Time = Label(root,font=("ds-digital",80),background="black",foreground="lime")
Time.pack(anchor="center")

Date = Label(root,font=("ds-digital",50),background="black",foreground="lime")
Date.pack(anchor="center")

Day = Label(root,font=("ds-digital",50),background="black",foreground="lime")
Day.pack(anchor="center")

clock()
mainloop()
