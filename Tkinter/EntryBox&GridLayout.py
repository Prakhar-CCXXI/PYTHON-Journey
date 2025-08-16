# step 1 : import tkinter
from tkinter import *
# step 2 : gui interaction
window = Tk()
# step 3 : adding input
window.title("Simple")
window.geometry("250x50")

label1=Label(window , text="mail")
label2=Label(window, text="password")

e1 = Entry(window,width=40,borderwidth=5)
label1.grid(row=0,column=1)
label2.grid(row=1,column=1)
e1.grid(row=0,column=2)


# step 4 : main loop
mainloop()
