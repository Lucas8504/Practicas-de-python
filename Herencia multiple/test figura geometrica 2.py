from rectangulo import Rectangulo

rectangulo1 = Rectangulo(5,7,"rojo")
print(rectangulo1.ancho)
print(rectangulo1.alto)
print(rectangulo1.color)
print(rectangulo1.calcular_area())

# MRO Method Resolution Order
print(Rectangulo.mro())
