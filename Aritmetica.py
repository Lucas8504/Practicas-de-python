class Aritmetica:
    """
    Clase aritmetica para sumar, restar, ect
    """

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def Sumar(self):
        return self.operandoA + self.operandoB

    def Restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5, 3)
print(f"suma = {aritmetica1.Sumar()}")
print(f"resta = {aritmetica1.Restar()}")
print(f"Multiplicacion = {aritmetica1.multiplicar()}")
print(f"Divicion = {aritmetica1.dividir()}")
