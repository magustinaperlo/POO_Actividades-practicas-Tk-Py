from tkinter import *



def factorial():
    n=1
    fact = 1
    for i in range (1, n+1):
        fact = fact * i
        
    return fact

#     nfact = n
#     return nfact

ventana = Tk()
ventana.geometry("600x200")
ventana.title("Factorial")
ventana.config(bg="grey")


frameFact = Frame(ventana)
frameFact.place(bordermode="inside", relx= 0.5, rely=0.5, anchor=CENTER)

etiqueta1 = Label(frameFact, text="n")
etiqueta1.grid(row=0, column=0)

lineEdit1 = Entry(frameFact,state="readonly")
lineEdit1.grid(row=0, column=1)

etiqueta2 = Label(frameFact, text="Factorial(n)")
etiqueta2.grid(row=0, column=2)

lineEdit2 = Entry(frameFact, state="readonly")
lineEdit2.grid(row=0, column=3)

buttonSiguiente = Button(frameFact, text="Siguiente")
buttonSiguiente.grid(row=0, column=4)


ventana.mainloop()