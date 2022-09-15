from tkinter import *

#Ventana principal
ventana = Tk()
ventana.geometry("600x200")
ventana.title("Factorial")
ventana.config(bg="lightgrey")

#Funcion Factorial
def factorial():
    numN=1+int(lineEdit1.get())
    numF=1
    for i in range (1, numN+1):
        numF = numF * i
    txt1.set(numN)
    txt2.set(numF)

#Al estar readonly lineEdit1 y 2, se debe usar StringVar.
txt1 =  StringVar()
txt2 =  StringVar()
txt1.set(1)
txt2.set(1)

#Frame centrado, ubicaremos todos los widgets aqui.
frameFact = Frame(ventana)
frameFact.place(relx= 0.5, rely=0.5, anchor=CENTER)

#Texto "n"
etiqueta1 = Label(frameFact, text="n")
etiqueta1.grid(row=0, column=0)

#Campo 1, "n". No editable.
lineEdit1 = Entry(frameFact,state="readonly", textvariable=txt1)
lineEdit1.grid(row=0, column=1)

#Texto "Factorial"
etiqueta2 = Label(frameFact, text="Factorial(n)")
etiqueta2.grid(row=0, column=2)

#Campo 2, resultado. No editable.
lineEdit2 = Entry(frameFact, state="readonly", textvariable=txt2)
lineEdit2.grid(row=0, column=3)

#Boton siguiente.
buttonSiguiente = Button(frameFact, text="Siguiente", command=factorial)
buttonSiguiente.grid(row=0, column=4)


ventana.mainloop()