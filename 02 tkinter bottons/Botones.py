import tkinter as tk

# importamos el modulo del tema de tkiter
from tkinter import ttk

windows = tk.Tk()

windows.geometry('600x400')

windows.title('Hola Mundo')
# agregamos un icono
windows.iconbitmap('icono.ico')

# Creamos un boton (winget) donde el objeto padre es windows
boton1 = ttk.Button(windows, text="Dar click")
# Usar el pack layout manager para ver el boton en la ventana
boton1.pack()


windows.mainloop()
