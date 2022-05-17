class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas


    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
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