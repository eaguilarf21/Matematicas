#hallar el area y perimetro de un circulo

import math

#entrada
print("ingresa el radio")
radio = float(input())

#proceso
area = math.pi*math.pow(radio,2)
perimetro = 2*math.pi*radio

#salida
print("El area del circulo es:", area)
print("El perimetro del circulo es:", perimetro)