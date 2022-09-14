import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("ContDecreciente.py")

frameCont = tk.Frame(ventana)
frameCont.place(relx= 0.5, rely=0.5, anchor=tk.CENTER)
num = 0

etiquetaNom = tk.Label(frameCont, text="Contador")
etiquetaNom.grid(row=0, column=0)
etiquetaCont = tk.Label(frameCont, text=num)
etiquetaCont.grid(row=0, column=1)

def contador():
    num=int(etiquetaCont.cget("text"))
    num -= 1
    etiquetaCont["text"] = num
    return num

botonCont = tk.Button(frameCont, text="-", command = contador)
botonCont.grid(row=0, column=2)

ventana.mainloop()