from tkinter import *

#Ventana Principal
ventana = Tk()
ventana.geometry("300x200")
ventana.title("ContCreciente")
ventana.config(bg="lightgrey")


#Funcion de contador +1
def contador():
    num=int(etiquetaCont.get())
    num += 1
    txtvar.set(num)

#Convertimos variable a StringVar para usar en Entry, textvariable.
txtvar=StringVar()
txtvar.set(0) # <- Seteamos a 0 el contador

#Frame, donde insertaremos todos los widgets.
frameCont = Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=CENTER) #Centramos y anclamos al centro

#Etiqueta "Contador"
etiquetaNom = Label(frameCont, text="Contador")
etiquetaNom.grid(row=0, column=0)

#Campo de numero, no editable.
etiquetaCont = Entry(frameCont, state="readonly", textvariable=txtvar)
etiquetaCont.grid(row=0, column=1)

#Boton Contador
botonCont = Button(frameCont, text="+", command = contador)
botonCont.grid(row=0, column=2)

ventana.mainloop()