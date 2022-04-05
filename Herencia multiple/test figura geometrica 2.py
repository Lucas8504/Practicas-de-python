from rectangulo import Rectangulo

rectangulo1 = Rectangulo(5, 7, "rojo")
print(f"Area del rectangulo: {rectangulo1.calcular_area()}")
print(rectangulo1)

# MRO Method Resolution Order
print(Rectangulo.mro())
