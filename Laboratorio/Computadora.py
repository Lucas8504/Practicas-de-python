from Laboratorio.Monitor import Monitor
from Laboratorio.Raton import Raton
from Laboratorio.Teclado import Teclado


class Computadora:
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        
        Id CPU: {self._id_computadora}/
        Nombre: {self._nombre}/
        Monitor: {self._monitor}/
        Teclado: {self._teclado}/
        Raton: {self._raton}
        
        """
if __name__ == "__main__":
        teclado1 = Teclado("HP", "USB")
        raton1 = Raton("Genius","USB")
        monitor1 = Monitor("LG", 27)
        computadora1 = Computadora("Asus",monitor1, teclado1, raton1)
        print(computadora1)
        teclado2 = Teclado("Logitech", "wireles")
        raton2 = Raton ("Logitech", "wireles")
        monitor2 = Monitor("Noblex", 27)
        computadora2 = Computadora("AMD cuant", monitor2, teclado2, raton2)
        print(computadora2)