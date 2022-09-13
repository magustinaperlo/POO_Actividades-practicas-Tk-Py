from tkinter import *

def contadorCreciente():
    num += 1
    return num

class contCreciente(Frame):
    pass

contCreciente = Tk()
contCreciente.title("ContCreciente")
contCreciente.resizable(False, False)
contCreciente.config(cursor="top_left_arrow")
root = contCreciente(contCreciente).grid()
contCreciente.mainloop()