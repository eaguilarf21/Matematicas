#hallar el area y perimetro de un circulo

import math

#entrada
print("ingresa el radio del circulo")
radio = float(input())

#proceso
area = math.pi*math.pow(radio,2)
perimetro = 2*math.pi*radio

#salida
print("el area del ciculo es:", area)
print("el perimetro del circulo es:", perimetro)