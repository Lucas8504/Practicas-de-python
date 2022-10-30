import tkinter as tk

# importamos el modulo del tema de tkiter
from tkinter import ttk

windows = tk.Tk()

windows.geometry('600x400')

windows.title('Hola Mundo')
# agregamos un icono
windows.iconbitmap('icono.ico')

# comfig Del gridmanager
windows.rowconfigure(0, weight=1)
windows.rowconfigure(1, weight=5)
windows.columnconfigure(0, weight=1)
windows.columnconfigure(1, weight=5)


#Metodos de los eventos
def evento1():
    boton1.config(text='Boton 1 precionado')

def evento2():
    boton2.config(text='boton 2 precionado')

# Definimos boton 1
boton1 = ttk.Button(windows, text='boton 1', command=evento1)
boton1.grid(row=0, column=0)

# Definimos boton 2
# *dsticky N(arriba), E(derecha), S(abajo), W(izquierda)
boton2 = ttk.Button(windows, text='boton 2', command=evento2)
boton2.grid(row=1, column=0, sticky='NSWE')  # *

# Definimos boton 3
boton3 = ttk.Button(windows, text="boton 3")
boton3.grid(row=0, column=1, sticky="NSWE")

# definimos boton 4
boton4 = ttk.Button(windows, text="boton 4")
boton4.grid(row=1, column=1)


windows.mainloop()