from tkinter import *
#Ventana principal
main = Tk()
main.geometry("500x200")

#Frame
juegoFr= Frame(main)
juegoFr.pack()

#Variable
numJuegos=StringVar()
numJuegos.set(0)

numBuenos=StringVar()
numBuenos.set(0)

numMalos=StringVar()
numMalos.set(0)

num1form=StringVar()
num1form.set("")

num2form=StringVar()
num2form.set("")

numRform=StringVar()
numRform.set("")

radioOption= IntVar()



#Forms
formNum1 = Entry(juegoFr, textvariable=num1form)
formNum1.grid(row = 0, column=0)

formNum2 = Entry(juegoFr, textvariable=num2form)
formNum2.grid(row = 0, column=2)

formResultado = Entry(juegoFr, textvariable=numRform)
formResultado.grid(row = 3, column=3)

#Boton

nuevoBoton = Button (juegoFr, text="Nuevo Numero")
nuevoBoton.grid(row= 1, column=3)

resultadoBoton = Button (juegoFr, text="Resultado")
resultadoBoton.grid(row= 4, column=3)

#Labels

menos = Label(juegoFr, text="-")
menos.grid(row=0, column=1)

lblJuegos=Label(juegoFr, text="Juegos")
lblJuegos.grid(row=6,column=3)
lblNum1 = Label(juegoFr, textvariable=numJuegos)
lblNum1.grid(row=6,column=4)

lblBuenos=Label(juegoFr, text="Buenos")
lblBuenos.grid(row=7,column=3)
lblNum1 = Label(juegoFr, textvariable=numBuenos)
lblNum1.grid(row=7,column=4)

lblMalo=Label(juegoFr, text="Malos")
lblMalo.grid(row=8,column=3)
lblNum1 = Label(juegoFr, textvariable=numMalos)
lblNum1.grid(row=8,column=4)

#Radio Botones

radSumar = Radiobutton(juegoFr,text= "Sumar", variable=radioOption, value=1)
radSumar.grid(row=1, column=0)

radRestar = Radiobutton(juegoFr,text= "Restar", variable=radioOption, value=2)
radRestar.grid(row=2, column=0)

radProducto = Radiobutton(juegoFr,text= "Producto", variable=radioOption, value=3)
radProducto.grid(row=3, column=0)

radDivision = Radiobutton(juegoFr,text= "Division", variable=radioOption, value=4)
radDivision.grid(row=4, column=0)

main.mainloop()