class MiClase:

    variables_clase = "valor variable clase"

    def __init__(self, variable_instancia):
        self.variables_instancia = variable_instancia

    @staticmethod
    def metodo_statico():   # los metodos estaticos no acceden a las variables de instancia pero si tienen relacion con la clase
        print("""
        Metodo estatico
        """)
        print(MiClase.variables_clase)

    @classmethod
    def metodo_clase(cls):
        print("""
        Metodo de clase (cls)
        """)
        print(cls.variables_clase)  # Los metodos de clase pueden acceder a las variables de clase

    def metodo_instancia(self):
        print("""Metodo de instancia
        """)
        self.metodo_clase()
        self.metodo_statico()


print(MiClase.variables_clase)
miClase = MiClase("valor variable instancia")
print(miClase.variables_instancia)
print(miClase.variables_clase)

MiClase.variables_clase2 = "alor variable clase 2"

miClase2 = MiClase("Otro valor de variable de instancia")
print(miClase2.variables_instancia)
print(miClase2.variables_clase)
print(miClase.variables_clase2)

MiClase.metodo_statico()

MiClase.metodo_clase()

miObjeto1 = MiClase("variable_instancia")
miObjeto1.metodo_clase()
miObjeto1.metodo_instancia()