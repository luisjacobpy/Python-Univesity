# 1 Vamos a declarar las variables
operandoA = 3
operandoB = 2

#Operaciones
add = operandoA + operandoB
resta = operandoA - operandoB
multiplicacion = operandoA * operandoB
division = operandoA / operandoB
modulo = operandoA % operandoB
exponente = operandoA ** operandoB
#Suma
print("Resultado de la suma:", add)
# 2 Existe otra forma de mandar a imprimir la información
print(f"Resultado de la suma: {add}")
# 3 a esto se le llama interpolación.
# Resta
print(f"Resultado de la resta: {resta}")
# Multiplicacion
print(f"Resultado de la multiplicación: {multiplicacion}")
# División
print(f"Resultado de la división: {division}")
#Para que la división nos devuelva un valor entero hacemos los siguiente
division_entero = operandoA // operandoB
print(f"Resultado de la división (int): {division_entero}")
# Modulo: Resultado residuo división (módulo)
print(f"Resultado residuo división (módulo): {modulo}")
#Exponente
print(f"Resultado del exponente: {exponente}")
