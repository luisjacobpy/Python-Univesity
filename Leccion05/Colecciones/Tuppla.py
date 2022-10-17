#Definir una  TUPLA
frutas = ("Naranja", "Platano", "Guayaba")

#Saber el largo de una tupla
print(len(frutas))
print(frutas)
print("Para visualizar el indice:")
print(frutas[1])

print("Para navegación inversa:")
print(frutas[-1])
print(frutas[2])

#RECORRER LOS ELEMENTOS DE UNA TUPLA CON CICLO FOR
for fruta in frutas:
    print(fruta, end=" ") #Para imprimir el ciclo en una sola linea, se utiliza "end"

#Cambiar el valor de una tupla
#Modificar una tupla a una lista, luego la regresamos a una tupla
frutasLista = list(frutas)
frutasLista[0] = "Pera"
frutas = tuple(frutasLista)
print("\n",frutas) #Para incluir un salto de linea
#Para eliminar una tupla
del frutas
print(frutas)