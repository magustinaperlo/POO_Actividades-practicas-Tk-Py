from tkinter import *

#Ventana principal
ventana = Tk()
ventana.geometry("600x200")
ventana.title("Contador")
ventana.config(bg="lightgrey")

#Convertimos campoNum, en StringVar. Se usa en Entry, textvariable.
campoNum = StringVar()
campoNum.set(0) # <- Seteamos a 0


#Funciones +1, -1, reset.
def FcountUp():
    num=int(campo.get())
    num += 1
    campoNum.set(num)

def FcountDown():
    num=int(campo.get())
    num -= 1
    campoNum.set(num)

def Freset():
    num = 0
    campoNum.set(num)

#Frame centrado, ubicaremos todos los widgets aqui.
frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=CENTER)

#Texto Contador
textoContador = Label(frameCont, text="Contador")
textoContador.grid(row=0, column=0)

#Campo de numeros, no editable
campo = Entry (frameCont, state="readonly", textvariable=campoNum)
campo.grid(row=0, column=1)

#Boton Up
countUp = Button (frameCont, text="Count Up", command=FcountUp)
countUp.grid(row=0, column=2)

#Boton Down
countDown = Button (frameCont, text="Count Down", command=FcountDown)
countDown.grid(row=0, column=3)

#Boton Reset
reset = Button(frameCont, text="Reset", command=Freset)
reset.grid(row=0, column=4)



ventana.resizable(False,False)
ventana.mainloop()