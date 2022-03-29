class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print("llamando metodo get nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("llamando metodo set nombre")
        self._nombre = nombre

    def Mostrar_detalle(self):
        print(f"persona: {self._nombre}, {self.apellido} {self.edad}")

persona1 = Persona("pedro", "garcia", 28)
persona1.nombre = "jose venitez"
print(persona1.nombre)