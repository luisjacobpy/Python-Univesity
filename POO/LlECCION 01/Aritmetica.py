class Aritmetica:
    # DocString = Documentación de la Clase en Python

    """
    Clase de Aritmetica para realizar las operaciones de Sumar, Restar, etc.
    """
# Método dunder init
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # Vamos a definir nuestro metodo sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB
    def division(self):
        return self.operandoA / self.operandoB

# Se crean los objetos de la clase Aritmetica
aritmetica1 = Aritmetica(5,3)
print(f'Suma: {aritmetica1.sumar()}')
print(f'Resta: {aritmetica1.restar()}')
print(f'Moltiplicación: {aritmetica1.multiplicar()}')
print(f'División: {aritmetica1.division():.2f}') #Se agrega para determinar el numero de puntos flotantes
