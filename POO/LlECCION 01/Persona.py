class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre}, {self._apellido},') #La variable self solo dse encuentra dentro de la definicion de la clase.
#Destructor
    def __del__(self):
        print(f'Persona:{self._nombre} {self._apellido}')

#Si se ejecuta dese otro archivo no se ejecuta el codigo.
if __name__ == "__main__":
    persona1 = Persona('Juan', 'Perez', 28)
#Si al imprimir aparece main, significa que estamos mandando a imprimir desde este mismo archivo
    print(__name__)