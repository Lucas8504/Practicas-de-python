from Laboratorio.Computadora import Computadora
from Laboratorio.Monitor import Monitor
from Laboratorio.Orden import Orden
from Laboratorio.Raton import Raton
from Laboratorio.Teclado import Teclado

teclado1 = Teclado("HP", "USB")
raton1 = Raton("Genius","USB")
monitor1 = Monitor("LG", 27)
computadora1 = Computadora("Asus",monitor1, teclado1, raton1)

teclado2 = Teclado("Logitech", "wireles")
raton2 = Raton ("Logitech", "wireles")
monitor2 = Monitor("Noblex", 27)
computadora2 = Computadora("AMD cuant", monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)