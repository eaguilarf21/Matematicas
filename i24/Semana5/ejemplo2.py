#calcular la raiz cubica de un numero
import math

#entrada
print("ingrese tu numero")
numero = float(input())

#proceso
rc = math.pow(numero, 1/3)

#salida
print("la raiz cubica de", numero, "es:",rc)