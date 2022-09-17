from tkinter import *

ventana= Tk()
ventana.geometry("350x350")
ventana.title("Calculadora 2")

calcuFr = Frame(ventana)
calcuFr.pack()

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
enResultado = Entry(calcuFr)
enResultado.grid(row=3, column=1)

#Botones Radio

radSumar = Radiobutton(calcuFr,value=1, text= "Sumar")
radSumar.grid(row=1, column=2)
radRestar = Radiobutton(calcuFr,value=2, text= "Restar")
radRestar.grid(row=2, column=2)
radProducto = Radiobutton(calcuFr,value=3, text= "Producto")
radProducto.grid(row=3, column=2)
radDivision = Radiobutton(calcuFr,value=4, text= "Division")
radDivision.grid(row=4, column=2)

#Botones

botCalcular = Button(calcuFr, text="Calcular")
botCalcular.grid(row=5, column=1)


ventana.mainloop()
