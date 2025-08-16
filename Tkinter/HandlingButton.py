from tkinter import *

window = Tk()
window.title("Simple")

def log_entry():
    print("Logged In")


button=Button(window,text="LOGIN",command=log_entry)
button.pack()

window.mainloop()