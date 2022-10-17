#Variables
calificacion = int(input("""
Bienvenido al sistema de calificaciones
Coloca aquí tu calificación del 1 al 10: 
"""))

letra = None
#Condicionales
if 9 <= calificacion <= 10:
    letra = "A"
elif 8 <= calificacion < 9:
    letra ="B"
elif 7 <= calificacion < 8:
    letra ="C"
elif 6 <= calificacion < 7:
    letra ="D"
elif 0 <= calificacion < 6:
    letra ="F"
print(f"¡Felicidades! obtuviste una {letra}.")