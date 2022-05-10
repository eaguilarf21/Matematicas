#Leer un numero entero y determine si es neutro, positivo o negativo

#entrada
print("ingrese el numero")
num = int(input())

#proceso
if num == 0:#neutro
    rpta = "el numero es neutro"
elif num>0:#positivo
    rpta= "el numero es positivo"
else:#negativo
    rpta= "el numero es negativo"

#salida
print(rpta)