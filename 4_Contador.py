from tkinter import *

ventana = Tk()
ventana.geometry("600x200")
ventana.title("Contador")
ventana.config(bg="grey")

campoNum = StringVar()
campoNum.set(0)

#Frame centrado, ubicaremos todos los elementos aqui.
frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=CENTER)

#Texto Contador
textoContador = Label(frameCont, text="Contador")
textoContador.grid(row=0, column=0)

#Campo de numeros
campo = Entry (frameCont, textvariable=campoNum)
campo.grid(row=0, column=1)

#Boton 1
countUp = Button (frameCont, text="Count Up")
countUp.grid(row=0, column=2)

#Boton 2
countDown = Button (frameCont, text="Count Down")
countDown.grid(row=0, column=3)

#Boton 3
reset = Button(frameCont, text="Reset")
reset.grid(row=0, column=4)


ventana.mainloop()