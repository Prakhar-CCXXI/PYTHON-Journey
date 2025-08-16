from tkinter import *

window = Tk()

c = Canvas(window,width=500 , height=500)
c.pack()

c.create_line(0,0,500,500,fill="green")
c.create_line(0,500,500,0, fill="blue")


mainloop()