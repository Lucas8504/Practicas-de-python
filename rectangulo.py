class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def CalcularArea(self):
        return f"Area del rectangulo: {self.base * self.altura}"


p = Rectangulo(int(input("Proporciona la base: ")), int(input("Proporciona la altura: ")))
print(p.CalcularArea())
