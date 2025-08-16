from tkinter import *

window = Tk()
window.geometry('500x500')

# Functionalities and Operations

def click(num):
    result = e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0,END)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0,END)

def mul():
    n1 = e.get()
    global math
    math = "multiply"
    global i
    i = int(n1)
    e.delete(0,END)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0,END)

# Buttons

e = Entry(window,width=56 , borderwidth=5 )
e.place(x=0,y=0)

b = Button(window,text='1',width= 12 , command = lambda:click(1))
b.place(x=0 , y=60)

b = Button(window,text='2',width= 12 , command = lambda:click(2))
b.place(x=90 , y=60)

b = Button(window,text='3',width= 12 , command = lambda:click(3))
b.place(x=180 , y=60)

b = Button(window,text='+',width= 8 , command= add )
b.place(x= 270 , y= 60)

b = Button(window,text='4',width= 12 , command = lambda:click(4))
b.place(x=0 , y=85)

b = Button(window,text='5',width= 12 , command = lambda:click(5))
b.place(x=90 , y=85)

b = Button(window,text='6',width= 12 , command = lambda:click(6))
b.place(x=180 , y=85)

b = Button(window,text='-',width= 8 , command= sub )
b.place(x=270 , y=85)

b = Button(window,text='7',width= 12 , command = lambda:click(7))
b.place(x=0 , y=110)

b = Button(window,text='8',width= 12 , command = lambda:click(8))
b.place(x=90 , y=110)

b = Button(window,text='9',width= 12, command = lambda:click(9))
b.place(x=180 , y=110)

b = Button(window,text='x',width= 8 , command= mul)
b.place(x=270 , y=110)

b = Button(window,text='0',width= 12 , command = lambda:click(0))
b.place(x=0 , y=135)

b = Button(window,text='00',width= 12 , command = lambda:click("00"))
b.place(x= 90, y=135)

# Evaluation and Clear

def equal():
    n2 = e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,i+int(n2))
    elif math == "subtraction":
        e.insert(0,i-int(n2))
    elif math == "multiplication":
        e.insert(0, i*int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))



b = Button(window,text='=',width= 12 , command=equal )
b.place(x=180 , y=135)

b = Button(window,text='/',width= 8 , command= div)
b.place(x= 270 , y = 135 )

def clear():
    e.delete(0,END)

b = Button(window,text='CLEAR',width= 45 , command=clear)
b.place(x= 5 , y = 160 )



mainloop()

