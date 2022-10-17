#Listas en python

#Podemos agregar cualquier tipo de fato
#Definir una lista de tipo string
nombres = ["Juan", "Karla", "Ricarco", "Maria"]
#Imprimir la lista de nombres
print(nombres)

#Acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
#Acceder a los elementos de manera inversa
print(nombres[-1]) #Para acceder al ultimo elemento de nuestra lista
print(nombres[-2]) #Para acceder al penultimo elemento de nuestra lista

#IMPRIMIR UN RANGO
print(nombres[0:2]) # Sin incluir el indice 2
#Ir del inicio de la lista al índice (sin incluirlo)
print(nombres[:3])
#Desde el indice indicado hasta el final
print(nombres[1:])
#CAMMBIAR UN VALOR DE NUESTRA LISTA
nombres[3] = "Ivone"
print(nombres)
#Iterar una lista

for nombre in nombres:
    print(nombre)
else:
    print("No existen mas nombres en la lista")

#Preguntar el largo de una lista
print(len(nombres))
#Agregar un elemento
nombres.append("Lorenzo")
print(nombres)
#Insertar un elemento en un indice proporcionado
nombres.insert(1, "Octavio")
print(nombres)
#Remover un elemento
nombres.remove("Octavio")
print(nombres)
#Remover el ultimo valor agregado
nombres.pop()
print(nombres)
#Eliminar un indice
del nombres [0]
print(nombres)
#Limpiar lista
nombres.clear()
print(nombres)
#Borrar la lista por completo de la memoria
del nombres
print(nombres)