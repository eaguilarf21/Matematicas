#ejemplo1: leer un numero y hallar su raiz cuadrada

import math

#entrada
print("ingrese su numero")
numero = float(input())

#proceso
#resultado = numero**(1/2)  #resultado = math.pow(numero,1/2) 
resultado = math.sqrt(numero) 

#salida
print("la raiz cuadrada del numero es:",resultado)