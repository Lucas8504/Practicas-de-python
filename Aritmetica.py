class Aritmetica:
    """
    Clase aritmetica para sumar, restar, ect
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def Sumar(self):
        return self.operandoA + self.operandoB

aritmetica1 = Aritmetica(5,3)
print(aritmetica1.Sumar())