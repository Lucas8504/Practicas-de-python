class Persona:                                 # clase persona
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):                         # metodo que imprime los datos
        return f"""
        nombre: {self.nombre}   Edad: {self.edad}
"""


class Empleado(Persona):                        # clase empleado que hereda a persona
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        if sueldo > 3000:                       # condicional que determina el pago de impuestos
            print("""
            Usted debe pagar impuestos.""")
        else:
            print("""
            Usted no debe pagar impuestos.""")


p = Persona(input("Escriba un nombre: "), input("Escriba una edad: "))
print(p.__str__())

nombre1 = input("Escriba un nombre: ")
edad1 = input("Escriba una edad: ")

while True:                                      # bucle con instrucciones de manejo de error
    try:
        sueldo1 = int(input("Indique el sueldo: "))
        e = Empleado(nombre1, edad1, sueldo1)
        break
    except:
        print("""
        Error! ingrese la cifra correcta.
        """)