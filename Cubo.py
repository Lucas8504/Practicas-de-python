class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def CalcularVolumen(self):
        return f"El volumen del cubo es: {self.ancho * self.alto * self.profundo}"

C = Cubo(int(input("Ingresa el ancho: " )), int(input("Ingresa el alto: ")), int(input("Ingresa la profundidad: ")))
print(C.CalcularVolumen())