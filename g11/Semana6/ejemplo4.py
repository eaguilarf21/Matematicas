#si ingreso dos numeros diferentes, sumarlos;
# si son iguales, multiplicarlos

#entrada
print("ingrese primer numero")
nume1 = float(input())
print("ingrese segundo numero")
nume2 = float(input())

#proceso
if nume1 != nume2:
    result = nume1+nume2

if nume1==nume2:
    result = nume1*nume2

#salida
print("El resultado es:",result)
