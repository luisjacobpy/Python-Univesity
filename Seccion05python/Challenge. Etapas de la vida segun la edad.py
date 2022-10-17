
#Asignacion de variables
edad =int(input("¿Cuál es tu edad?: "))
mensaje = None

#Condiciones
#if edad >= 0 and edad < 10
if 0 <= edad < 10:
    mensaje = "La infancia es increible"
elif 10 <= edad < 20:
    mensaje = "Muchos cambios, mucho estudio..."
elif 20 <= edad < 30:
    mensaje = "Amor y comienza el trabajo"
else:
    mensaje = "Estapa de vida no reconocida"

print(f"Tu edad es: {edad} años,{mensaje}")