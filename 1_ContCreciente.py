from tkinter import *



class contCreciente(Frame):
    def __init__(self, master, *x,**y):
        Frame.__init__(self, master, *x, **y)
        self.parent = master
        self.grid()
        self.createWidgets()
        
    def contadorCreciente(self, num):
        num += 1
        Label(text=num,font=('Consolas 13 bold')).pack()
    
    # def sumarButton(self):
    #     self.num == num
    #     num += 1
    #     return num
        

    def createWidgets(self):
        self.display = Label(self, font=("Consolas", 18), relief=GROOVE, justify=CENTER, bg='white', fg='blue', borderwidth=2)
        # self.display.insert(0, "0")
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.sumarButton = Button(self, font=("Consolas", 12), fg='red', text="Sumar +1", highlightbackground='red', command=lambda: contadorCreciente("1"))
        self.sumarButton.grid(row=1, column=0, sticky="nsew")



    

contadorP = Tk()
contadorP.title("ContCreciente")
contadorP.resizable(False, False)
contadorP.config(cursor="top_left_arrow")
root = contCreciente(contadorP).grid()
contadorP.mainloop()