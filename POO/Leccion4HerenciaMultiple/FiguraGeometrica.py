#ABC Abstract base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __int__(self, ancho, alto): # Definimos los parametros ancho y alto
        if self._validar_valor(ancho):
        #if 0 < ancho < 10: #Validamos si la variable de ancho se encuentra entre 0 y 10
        # Encapsulamos
            self._ancho = ancho  # Declaramos que el atributo es igual al argumento edad
        else:
            self._ancho = 0 # Asignamos el valor de 0 ya que no paso la validación
            print(f'Valor erroneo ancho {ancho}')
        if self._validar_valor(alto):
        #if 0 < alto < 10:
            self._alto = alto
        else:
            self._alto = 0 # Asignamos el valor de 0 ya que no paso la validación
            print(f'Valor erroneo alto {alto}')
    #  Metodo Get // Encapsulamos el atributo
    @property
    def ancho(self):
        return self._ancho
    # Set / para modificar el valor
    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho): # Validación en el metodo set
            self._ancho = ancho
        else:
            print(f"Valor erroneo ancho {ancho}")

    # Get
    @property
    def alto(self):
        return self._alto
    #Set
    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto): # Validación en el metodo set
            self._alto = alto
        else:
            print(f"Valor erroneo alto: {alto}")

    @abstractmethod
    def calcular_area(self):
        pass


    def __str__(self):
        return f"FiguraGeometrica [Ancho: {self._ancho}: Alto: {self._alto} ]"

    #Metodo encapsulado
    def _validar_valor(self, valor):
        return True if 0 < valor < 10 else False

