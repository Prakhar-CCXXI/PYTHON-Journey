import socket
from tkinter import *

def send(listbox, entry):
    message = entry.get()
    listbox.insert('end', "Server: " + message)
    entry.delete(0, END)
    client.send(message.encode("utf-8"))

def recieve(listbox):
    message_to_client = client.recv(50)
    listbox.insert('end', "Client: " + message_to_client.decode('utf-8'))

root = Tk()

entry = Entry(root)
entry.pack(side=BOTTOM)

listbox = Listbox(root)
listbox.pack()

button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=BOTTOM)

rbutton = Button(root, text="Receive", command=lambda: recieve(listbox))  # Fixed to call 'recieve'
rbutton.pack(side=BOTTOM)

root.title('Server')

# --- Socket Server Part ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))
s.listen(4)

client, address = s.accept()
print(f"Connection from {address}")

root.mainloop()
