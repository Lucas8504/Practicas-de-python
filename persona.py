class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def Mostrar_detalle(self):
        print(f"persona: {self.nombre}, {self.apellido} {self.edad}")


persona1 = Persona("pedro", "garcia", 30, 1122334455, 7, 7, 8, m= "auto", p= "elicoptero")
persona1.Mostrar_detalle()

persona2 = Persona("Karla", "Gomez", 30)
persona2.Mostrar_detalle()