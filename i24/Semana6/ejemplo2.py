#Dada una nota, determinar si aprobo

#entrada
print("ingrese su nota")
nota = float(input())

#proceso
mensaje = ""
if nota >= 12.5:
    mensaje = "aprobo"

#salida
print(mensaje)