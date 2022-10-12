import tkinter as tk

# importamos el modulo del tema de tkiter
from tkinter import ttk

windows = tk.Tk()

windows.geometry('600x400')

windows.title('Hola Mundo')
# agregamos un icono
windows.iconbitmap('icono.ico')


#Metodos de los eventos
def evento1():
    boton1.config(text='Boton 1 precionado')

# Definimos 2 botones
boton1 = ttk.Button(windows, text='boton 1', command=evento1)
boton1.grid(row=0, column=0)


windows.mainloop()