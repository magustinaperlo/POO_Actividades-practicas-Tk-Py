from tkinter import *

#Ventana
ventana = Tk()
ventana.geometry("600x400")
ventana.title("Peliculas")

framePeli = Frame(ventana)
framePeli.pack()

tituloPeliculatxt = Label(framePeli, text="tituloPeliculatxt")
tituloPeliculatxt.pack()
peliculastxt = Label(framePeli, text="peliculastxt")
peliculastxt.pack()
peliculasform = Entry(framePeli, textvariable="peliculasform")
peliculasform.pack()
peliculaslist = Listbox(framePeli)
peliculaslist.pack()
addPelicula = Button(framePeli, text="addPelicula")
addPelicula.pack()

ventana.resizable(False, False)
ventana.mainloop()