#leer un numero entero y determinar si es par o impar

#entrada
print("Ingrese el numero")
numero = float(input())
#proceso
if numero % 2 == 0:
    result ="el numero es par"
else:
    result = "el numero es impar"

#salida
print(result)