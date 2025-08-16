from tabnanny import check
from tkinter import *

window = Tk()

window.geometry("500x500")

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window,text="apple", onvalue= 1 , offvalue= 0 , height= 2 , width= 10)

chk_btn_1.pack()


mainloop()

