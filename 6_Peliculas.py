from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Peliculas")

#Funcion del boton
def addPelisF():
    a = peliculasform.get() #Se obtiene valor en Entry
    peliculaslist.insert(END, a) #Se inserta en Listbox
    peliculasform.delete(0, END) #Se limpia el campo

#Se asigna variable para usar en Entry
peliculasform = StringVar()
peliculasform.set("")

#Frame
framePeli = Frame(ventana)
framePeli.pack()

#Etiquetas
tituloPeliculatxt = Label(framePeli, text="Escribe el titulo de una pelicula")
tituloPeliculatxt.grid(row=0, column=0)

peliculastxt = Label(framePeli, text="Peliculas")
peliculastxt.grid(row=0, column=1)

#Entrada
peliculasform = Entry(framePeli, textvariable=peliculasform)
peliculasform.grid(row=1, column=0)

#Lista
peliculaslist = Listbox(framePeli)
peliculaslist.grid(row=1, column=1)

#Boton
addPelicula = Button(framePeli, text="Añadir", command=addPelisF)
addPelicula.grid(row=2, column=0)

#Ventana no ajustable
ventana.resizable(False, False)
ventana.mainloop()