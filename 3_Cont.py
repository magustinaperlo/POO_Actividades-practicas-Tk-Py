from tkinter import *

numN = 0
numF = 0


def factorial():
    numN=1+int(lineEdit1.get())
    numF=1
    for i in range (1, numN+1):
        numF = numF * i
    txt1.set(numN)
    txt2.set(numF)
    # return numF, numN






ventana = Tk()
ventana.geometry("600x200")
ventana.title("Factorial")
ventana.config(bg="grey")

txt1 =  StringVar()
txt2 =  StringVar()
txt1.set(1)
txt2.set(1)

frameFact = Frame(ventana)
frameFact.place(relx= 0.5, rely=0.5, anchor=CENTER)

etiqueta1 = Label(frameFact, text="n")
etiqueta1.grid(row=0, column=0)

lineEdit1 = Entry(frameFact,state="readonly", textvariable=txt1)
lineEdit1.grid(row=0, column=1)

etiqueta2 = Label(frameFact, text="Factorial(n)")
etiqueta2.grid(row=0, column=2)

lineEdit2 = Entry(frameFact, state="readonly", textvariable=txt2)
lineEdit2.grid(row=0, column=3)

buttonSiguiente = Button(frameFact, text="Siguiente", command=factorial)
buttonSiguiente.grid(row=0, column=4)


ventana.mainloop()