#Importamos las clases que utilizaremos
# Clase hija con herencia multiple
from FiguraGeometrica import FiguraGeometrica
from Color import Color
#Clase
class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        FiguraGeometrica.__int__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'Objeto que toma atributos de la clase Rectangulo:{FiguraGeometrica.__str__(self)}: Objeto que toma atributos de la clase color: {Color.__str__(self)}'
