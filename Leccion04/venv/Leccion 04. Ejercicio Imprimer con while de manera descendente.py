#Imprimri numeros de 5 a 1 de manera descnedente
contador = 5
minimo = 1
while contador >= minimo:
    print(contador)
    #contador = contador - 1
    contador -= 1 #la variable de contador la estamos restando en 1: contador = contador + 1
else:
    print("Fin ciclo while")