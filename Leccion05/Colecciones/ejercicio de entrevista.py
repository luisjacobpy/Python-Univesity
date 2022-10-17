"""
1. Definir una función max que tome el argumento de dos numeros y devuelva el valor mayor de ellos
"""


def custom_max(n1: int, n2: int):
    """Dado dos numeros de entrada retornar el maximo de ambos

    Args:
        n1 (int): Primer numero a comparar
        n2 (int): Segundo numero a comparar

    Returns:
        int: Mayor de ambos

    """
    if n2 > n1:
        return n2
    elif n1 > n2:
        return n1
    elif n1 == n2:
        raise Exception("Los valores no pueden ser iguales")
    return n
print(custom_max(1,2))
print(custom_max(3,2))
