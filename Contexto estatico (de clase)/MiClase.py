class MiClase:

    vaiables_clase = "valor variable clase"

    def __init__(self, variable_instancia):
        self.vaiables_instancia = variable_instancia

    @staticmethod
    def metodo_statico():
        print("""
        Metodo estatico
        """)
        print(MiClase.vaiables_clase)

print(MiClase.vaiables_clase)
miClase = MiClase("valor variable instancia")
print(miClase.vaiables_instancia)
print(miClase.vaiables_clase)

MiClase.vaiables_clase2 = "alor variable clase 2"

miClase2 = MiClase("Otro valor de variable de instancia")
print(miClase2.vaiables_instancia)
print(miClase2.vaiables_clase)
print(miClase.vaiables_clase2)

MiClase.metodo_statico()