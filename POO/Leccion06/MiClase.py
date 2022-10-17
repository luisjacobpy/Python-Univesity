class MiClase:

    # Para asignar un atributo de Clase se crea un  variable de clase.
    variable_clase = "Valor variable clase"


    #Variable de instancia
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia


#Para acceder a una variable de clase no necesitamos un objeto
print(MiClase.variable_clase)
# Para poder acceder a una variable de instancia necesitamos crear un objeto.
miClase = MiClase("Valor variable instancia.")
print(miClase.variable_instancia)
# Desde el objeto podemos acceder TAMBIEN a una variable de clase.
print(miClase.variable_clase)

MiClase.variable_clase2 = "Valor variable clase 2"

miClase2 = MiClase("Otro valor de varible de instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)
# Podemos acceder a la la variable
print(MiClase.variable_clase2)
