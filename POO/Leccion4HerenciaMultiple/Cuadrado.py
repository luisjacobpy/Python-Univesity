# Importamos las clases que utilizaremos
# Clase hija con herencia multiple
from FiguraGeometrica import FiguraGeometrica
from Color import Color
from FiguraGeometrica import FiguraGeometrica
from Color import Color

# Definimos la clase cuadrado
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__int__(self, lado, lado)
        Color.__init__(self, color)
    # Definimos el metodo calcular area
    def calcular_area(self):
        return self.alto * self.ancho

    # Vamos Metodo STR  a sobreescribir a los metodos heredados de la clase padre
    def __str__(self):
        # En esta caso la clase hija no tiene atributos en particular
        # Mandamos llamar el Metodo STR de la clase hija
        return f'{FiguraGeometrica.__str__(self)}: {Color.__str__(self)}'