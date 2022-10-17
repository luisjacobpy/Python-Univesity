#Este es un ejemplo de set
planetas = {"marte", "jupiter", "venus"}
print(planetas)
#Para conocer el largo
print(len(planetas))
print("marte" in planetas)

#agregar un elemento
planetas.add("Tierra")
print(planetas)

#Recordemos que no soporta elementos duplicados

#La función tipo set nos puede servir para evitar elementos DUPLICAOS

#Eliminar elementos
planetas.remove("Tierra")
print(planetas)
#Laa función discard no arroja un error en caso de que el elemento no se encuentre disponible
planetas.discard("jupiter")
print(planetas)
#Limpiar set
planetas.clear()
#Elimidar set
del_planetas