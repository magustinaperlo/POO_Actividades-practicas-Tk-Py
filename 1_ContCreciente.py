import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")
ventana.title("ContCreciente.py")
num = 0

etiquetaCont = tk.Label(ventana, text=num)
etiquetaCont.pack()

def contador():
    num=int(etiquetaCont.cget("text"))
    num += 1
    etiquetaCont["text"] = num
    return num

botonCont = tk.Button(ventana, text="+1", command = contador)
botonCont.pack()

ventana.mainloop()