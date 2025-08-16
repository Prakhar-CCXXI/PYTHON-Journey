from tkinter import *

window = Tk()

menu = Menu(window)
file = Menu(menu , tearoff=0)
file.add_command(label = "New")
file.add_command(label="Open")
file.add_command(label = "Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Exit", command=window.quit)

menu.add_cascade(label ="File" , menu = file)
window.config(menu = menu)



mainloop()