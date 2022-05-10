#Leer dos numeros enteros y determine el numero mayor y menor

#entrada
print("ingrese el primer numero")
num1 = int(input())

print("ingrese el segundo numero")
num2 = int(input())

#proceso

if num1>num2:
    may = "el numero mayor es ",num1
else:
    may = "el numero mayor es ",num2

if num1<num2:
    men = "el numero menor es ",num1
else:
    men = "el numero menor es ",num2

#salida
print(may)
print(men)