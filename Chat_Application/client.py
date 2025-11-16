import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "You: " + message)
    entry.delete(0, END)
    s.send(message.encode('utf-8'))

def receive(listbox):
    try:
        message = s.recv(50)
        listbox.insert('end', "Server: " + message.decode('utf-8'))
    except Exception as e:
        listbox.insert('end', "Error receiving message: " + str(e))

root = Tk()

entry = Entry(root)
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Receive", command=lambda: receive(listbox))  # Fixed to call 'receive'
rbutton.pack(side=BOTTOM)

root.title('Client')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345
s.connect((HOST_NAME, PORT))

root.mainloop()
