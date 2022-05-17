class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona:{self.id_persona} Nombre:{self.nombre} Edad:{self.edad}"


persona1 = Persona("Marcos", 28)
print(" ")
print(persona1)
print(" ")
persona2 = Persona("Amanda", 25)
print(persona2)
print(" ")
persona3 = Persona("Eduardo", 24)
print(persona3)
print(" ")
print(f"Valor contador personas: {Persona.contador_personas}")