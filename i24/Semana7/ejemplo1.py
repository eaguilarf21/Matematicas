#dado un numero entero, determinar si es positivo o negativo

#
print("ingrese el numero entero")
numero = int(input())

#
if numero>0:
    rpta="el numero es positivo"
elif numero==0:
    rpta="el numero es cero"
else:#negativos
    rpta = "el numero es negativo"

#
print(rpta)