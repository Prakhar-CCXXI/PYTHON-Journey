# step 1 : import tkinter
from tkinter import *
# step 2 : gui interaction
window = Tk()
# step 3 : adding input
window.title("Simple")
window.geometry("500x500")
lable1 = Label(window , text="Lable1" , bg="red" , fg="white")
lable2 = Label(window,text="Lable2" , bg="blue",fg="white")

lable1.pack(side=TOP , fill=X , expand=False)
lable2.pack(side=LEFT,fill=Y,expand=False)




# step 4 : main loop
window.mainloop()
