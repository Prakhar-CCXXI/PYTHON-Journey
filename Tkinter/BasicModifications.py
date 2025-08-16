# step 1 : import tkinter
from tkinter import *
# step 2 : gui interaction
window = Tk()
# step 3 : adding input
window.title("Simple")
window.geometry("500x700")
window.config(bg = "black")
frame1 = Frame(window , bg = "red" , width=300 , height= 300 , cursor="dot")
frame2 = Frame(window , bg = "yellow" , width=300 , height= 300 , cursor="dotbox")
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)


# step 4 : main loop
mainloop()
