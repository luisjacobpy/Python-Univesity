
#Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Metodo str
    def __str__(self):
        return f"Persona[Nombre:{self.nombre}, Edad:{self.edad}]"
#Clase hija
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        #Metodo que nos permite acceder a los metodos de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        # Retornamos, accedemos al str de la clase padre con el metodo string
        return f"Sueldo: [{self.sueldo}]; {super().__str__()}, "

