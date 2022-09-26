from tkinter import *
from tkinter import messagebox

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#Ventana
ventana = Tk()
ventana.geometry("300x200")
ventana.title("Calculadora")

#Funciones
def validacion():
    a = num1.get()
    b = num2.get()
    if (a.isnumeric() or isfloat(a)) and (b.isnumeric() or isfloat(a)):
        pass 
    else:
        messagebox.showerror(title="ERROR CARACTER", message="Ha ingresado un caracter incorrecto")
def validacion2(a, b):
    if a.isnumeric():
        a =int(a)
    else:
        a=float(a)
    if b.isnumeric():
        b=int(b)
    else:
        b=float(b)
    return a , b
def sumaF():
    x= num1.get()
    y= num2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x+y
    numResultadovar.set(c)
def restaF():
    x= num1.get()
    y= num2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x-y
    numResultadovar.set(c)
def productoF():
    x= num1.get()
    y= num2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x*y
    numResultadovar.set(c)
def divisionF():
    x= num1.get()
    y= num2.get()
    validacion()
    x,y = validacion2(x, y) 
    if y == 0:
        msg="No se puede dividir por 0."
        numResultadovar.set(msg)
    else:
        c = x/y
        numResultadovar.set(c)
def modF():
    x= num1.get()
    y= num2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x%y
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
