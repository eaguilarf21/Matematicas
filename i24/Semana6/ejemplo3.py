#leer dos nombres de personas y determine si son iguales
#identificar la homonimia de dos personas
#dos personas son tocayos?

#entrada
print("ingrese el primer nombre")
nombre1 = str(input())
print("ingrese el segundo nombre")
nombre2 = input()

#proceso
mensaje=""
if nombre1==nombre2:
    mensaje = "hay homonimia"

#salida
print(mensaje)

#adicional
print(type(nombre1))
print(type(nombre2))