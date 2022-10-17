#Sintaxis de range(inicio<opcional>, fin<requerido>, incremento<opcional>)

#for letra in "Holanda":
#    if letra == "a":
#        print(f"La letra encontrada:{letra}")
#        break #Vamos a poder romper un cliclo for
#else:
 #   print("Fin del ciclo for")

# continue
#for i in range(6):
#    if i % 2 != 0:
 #       continue
 #   print(i)

#Ejercicio 1. Iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
for i in range(11):
    if i % 3 == 0:
        print(i)

print("Rango de numeros de 2 a 6")
#Ejercicio 2. Crear un rangop de numeros de 2 a 6, e imprimelos
for i in range(2, 7):
    print(i)
# Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2.
print("Ejercicio 3. Crear un rango de 3 a 10, pero con incremento de 2 en 2")
for i in range(3, 11, 2):
    print(i)
