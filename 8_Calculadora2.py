from tkinter import *
from tkinter import messagebox

#Ventana principal
ventana= Tk()
ventana.geometry("350x350")
ventana.title("Calculadora 2")

#Encuadre
calcuFr = Frame(ventana)
calcuFr.pack()

#Variables
radioOption = IntVar()
txtenResultado=StringVar()
txtenResultado.set("")


#Funciones

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def validacion():
    a = enValor1.get()
    b = enValor2.get()
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
    x= enValor1.get()
    y= enValor2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x+y
    txtenResultado.set(c)
def restaF():
    x= enValor1.get()
    y= enValor2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x-y
    txtenResultado.set(c)
def productoF():
    x= enValor1.get()
    y= enValor2.get()
    validacion()
    x,y = validacion2(x, y)
    c = x*y
    txtenResultado.set(c)
def divisionF():
    x= enValor1.get()
    y= enValor2.get()
    validacion()
    x,y = validacion2(x, y) 
    if y == 0:
        msg="No se puede dividir por 0."
        txtenResultado.set(msg)
    else:
        c = x/y
        txtenResultado.set(c)


def OperacionesCalc():
    varFunction = int(radioOption.get())
    if varFunction == 1:
        sumaF()
    elif varFunction == 2:
        restaF()
    elif varFunction == 3:
        productoF()
    elif varFunction == 4:
        divisionF()
    else:
        messagebox.showwarning("Error","Seleccione una operacion.")


#Etiquetas
lbValor1= Label(calcuFr, text="Valor 1")
lbValor1.grid(row=1,column=0)

lbValor2= Label(calcuFr, text="Valor 2")
lbValor2.grid(row=2,column=0)

lbResultado= Label(calcuFr, text="Resultado")
lbResultado.grid(row=3,column=0)

lbIoeraciones= Label(calcuFr, text="Operaciones")
lbIoeraciones.grid(row=0,column=2)


#Forms
enValor1 = Entry(calcuFr)
enValor1.grid(row=1, column=1)

enValor2 = Entry(calcuFr)
enValor2.grid(row=2, column=1)

enResultado = Entry(calcuFr, state="readonly", textvariable=txtenResultado)
enResultado.grid(row=3, column=1)


#Botones Radio
radSumar = Radiobutton(calcuFr,text= "Sumar", variable=radioOption, value=1)
radSumar.grid(row=1, column=2)

radRestar = Radiobutton(calcuFr,text= "Restar", variable=radioOption, value=2)
radRestar.grid(row=2, column=2)

radProducto = Radiobutton(calcuFr,text= "Producto", variable=radioOption, value=3)
radProducto.grid(row=3, column=2)

radDivision = Radiobutton(calcuFr,text= "Division", variable=radioOption, value=4)
radDivision.grid(row=4, column=2)


#Botone calcular
botCalcular = Button(calcuFr, text="Calcular", command=OperacionesCalc)
botCalcular.grid(row=5, column=1)

ventana.mainloop()