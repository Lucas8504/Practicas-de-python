class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def Mostrar_detalle(self):
        print(f"persona: {self.__nombre}, {self.apellido} {self.edad}")

persona1 = Persona("pedro", "garcia", 28)
persona1.__nombre = "pedro luis"
persona1.Mostrar_detalle()