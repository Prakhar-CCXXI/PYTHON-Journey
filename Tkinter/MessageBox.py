from tkinter import *

import tkinter.messagebox

window=Tk()
tkinter.messagebox.showerror("Info" , "Running out time")
question = tkinter.messagebox.askyesno("Weather","Will it rain?")

if question == True:
    print("Take an umbrella")
else:
    print("Okay")

mainloop()