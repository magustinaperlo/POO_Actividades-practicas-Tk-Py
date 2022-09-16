from calendar import c
from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry("300x200")
ventana.title("Calculadora")

#Funciones

def sumaF():
    a = int(num1.get())
    b = int(num2.get())
    c = a + b
    numResultadovar.set(c)
def restaF():
    a = int(num1.get())
    b = int(num2.get())
    c = a-b
    numResultadovar.set(c)
def productoF():
    a = int(num1.get())
    b = int(num2.get())
    c = a*b
    numResultadovar.set(c)
def divisionF():
    a = int(num1.get())
    b = int(num2.get())
    if b == 0:
        msg="No se puede dividir por 0."
        numResultadovar.set(msg)
    else:
        c = a/b
        numResultadovar.set(c)
def modF():
    a = int(num1.get())
    b = int(num2.get())
    c = a%b
    numResultadovar.set(c)
def clearF():
    num1var.set("")
    num2var.set("")
    numResultadovar.set("")

#------------------
#Frame
frameCalc = Frame(ventana)
frameCalc.pack()

#Asignacion de variables para Entry
num1var= StringVar()
num2var= StringVar()
numResultadovar= StringVar()
num1var.set("")
num2var.set("")
numResultadovar.set("")

#Textos
num1text=Label(frameCalc, text="Primer numero")
num1text.grid(row=0, column=0)

num2text=Label(frameCalc, text="Segundo numero")
num2text.grid(row=1, column=0)

resultadotext=Label(frameCalc, text="Resultado")
resultadotext.grid(row=2, column=0)

#Entradas
num1 = Entry(frameCalc, textvariable=num1var)
num1.grid(row=0, column=1)

num2 = Entry(frameCalc, textvariable=num2var)
num2.grid(row=1, column=1)

resultado = Entry(frameCalc, state="readonly", textvariable=numResultadovar)
resultado.grid(row=2, column=1)

#Botones
suma = Button(frameCalc, text="+", command=sumaF)
suma.grid(row=4, column=0)

resta = Button(frameCalc, text="-", command=restaF)
resta.grid(row=4, column=1)

producto = Button(frameCalc, text="*", command=productoF)
producto.grid(row=5, column=0)

division = Button(frameCalc, text="/", command=divisionF)
division.grid(row=5, column=1)

mod = Button(frameCalc, text="%", command=modF)
mod.grid(row=6, column=0)

clear = Button(frameCalc, text="CLEAR", command=clearF)
clear.grid(row=6, column=1)

ventana.resizable(False,False)
ventana.mainloop()
