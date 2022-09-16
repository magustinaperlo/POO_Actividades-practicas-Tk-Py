from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry("300x200")

#Frame
frameCalc = Frame(ventana)
frameCalc.pack()


#Textos
num1text=Label(frameCalc, text="Primer numero")
num1text.grid(row=0, column=0)

num2text=Label(frameCalc, text="Segundo numero")
num2text.grid(row=1, column=0)

resultadotext=Label(frameCalc, text="Resultado")
resultadotext.grid(row=2, column=0)

#Entradas
num1 = Entry(frameCalc, textvariable="0")
num1.grid(row=0, column=1)

num2 = Entry(frameCalc, textvariable="")
num2.grid(row=1, column=1)

resultado = Entry(frameCalc, state="readonly", textvariable="")
resultado.grid(row=2, column=1)

#Botones
suma = Button(frameCalc, text="+")
suma.grid(row=4, column=0)

resta = Button(frameCalc, text="-")
resta.grid(row=4, column=1)

producto = Button(frameCalc, text="*")
producto.grid(row=5, column=0)

division = Button(frameCalc, text="/")
division.grid(row=5, column=1)

mod = Button(frameCalc, text="%")
mod.grid(row=6, column=0)

clear = Button(frameCalc, text="CLEAR")
clear.grid(row=6, column=1)


ventana.mainloop()
