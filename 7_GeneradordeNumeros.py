from tkinter import *
from random import *

#Ventana principal
ventana = Tk()
ventana.geometry("300x150")
ventana.title("Generador de numeros")

def numRandom():
    a = int(formNum1.get())
    b = int(formNum2.get())
    if a > b:
        msg="ERROR. Num1 < Num2"
        numResultado.set(msg)
    else:
        c = randint(a,b)
        numResultado.set(c)

numResultado = StringVar()
numResultado.set("")

#Se crea y ubica frame
frameGen = Frame(ventana)
frameGen.pack()

#Etiquetas
txtNum1 = Label(frameGen, text="Número 1")
txtNum1.grid(row=0,column=0) 
txtNum2 = Label(frameGen, text="Número 2")
txtNum2.grid(row=1,column=0)
txtNumGen = Label(frameGen, text="Número Generado")
txtNumGen.grid(row=2,column=0)

#Caja de numeros y resultado
formNum1 = Spinbox(frameGen, from_= 0 ,to=999)  
formNum1.grid(row=0,column=1)
formNum2 = Spinbox(frameGen, from_= 0 ,to= 999) 
formNum2.grid(row=1,column=1)
formNumResultado = Entry(frameGen, state="readonly", textvariable=numResultado) 
formNumResultado.grid(row=2,column=1)

#Boton
btnGenerar = Button(frameGen, text="Generar", command=numRandom)
btnGenerar.grid(row=3, column=1)

ventana.mainloop()