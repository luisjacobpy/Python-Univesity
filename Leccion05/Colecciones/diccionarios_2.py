# dic (key, value)

diccionario = {
    "IDE": "Integrated Development Enviroment",
    "OOP": "Object oriented Programming",
    "DBMS": "Data base Managment System"

}
"""
Dentro de un diccionario no hay indices
"""
print(diccionario)
#Funcion para conocer el largo
print(len(diccionario))

#Para acceder a un elemento
print(diccionario["IDE"])

"""
Otra forma para para recuperar otro elemento
"""
print(diccionario.get("OOP"))
#MODIFICAR ELEMENTOS
diccionario["IDE"] = "integrate development enviroment"
print(diccionario)

#Recorrer los elementos de un diccionario

for termino, valor in diccionario.items():
    print(termino, valor)

#Imprimir solo Keys
for termino in diccionario.keys():
    print(f"Este es un termino: {termino}")

#Imprimir solo valores
for valor in diccionario.values():
    print(valor)

#Comprobar la existencia de algun elemento
print("IDE" in diccionario)


#Agregar un elemento
diccionario["PK"] = "Primary Key"

# Remover un elemento

diccionario.pop("DBMS")
print(diccionario)

#Para limpiar
diccionario.clear()
print(diccionario)
#Para eliminar el diccionario
del diccionario
print(diccionario)