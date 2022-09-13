from tkinter import *
root = Tk()
root.counter = 0

def clicked():
    root.counter += 1
    L['text'] = 'Contador: ' + str(root.counter)
        
b = Button(root, text="+1", command=clicked)
b.pack()

L = Label(root, text="Contador: 0")
L.pack()

root.mainloop()