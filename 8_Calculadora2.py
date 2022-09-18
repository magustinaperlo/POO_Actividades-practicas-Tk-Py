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
def sumaF():
    a = int(enValor1.get())
    b = int(enValor2.get())
    c = a + b
    txtenResultado.set(c)
def restaF():
    a = int(enValor1.get())
    b = int(enValor2.get())
    c = a-b
    txtenResultado.set(c)
def productoF():
    a = int(enValor1.get())
    b = int(enValor2.get())
    c = a*b
    txtenResultado.set(c)
def divisionF():
    a = int(enValor1.get())
    b = int(enValor2.get())
    if b == 0:
        msg="ERROR. Division por 0"
        txtenResultado.set(msg)
    else:
        c = a/b
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