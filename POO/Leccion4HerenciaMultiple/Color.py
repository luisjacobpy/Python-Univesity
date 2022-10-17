#Clase padre
class Color(object):
    def __init__(self, color):
        # Encapsulamos el atributo
        self._color = color

    # Get para recuperar
    @property
    def color(self):
        return self._color
    # Set
    @color.setter
    def color(self, color):
        self._color = color

    # STR
    def __str__(self):
        return f"Color [color: {self._color}]"

