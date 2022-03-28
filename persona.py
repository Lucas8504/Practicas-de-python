class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def Mostrar_detalle(self):
        print(f"persona: {self.nombre}, {self.apellido} {self.edad}")


persona1 = Persona(Juan, Perez, 28, 44553322, 2, 3, 5, m= "manzana", p= "pera")
persona1.Mostrar_detalle()

persona2 = Persona(Karla, Gomez, 30)
persona2.Mostrar_detalle()