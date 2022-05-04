#dado dos numeros, si son diferentes que se sumen,
# si son iguales calcula el producto

#entrada
print("ingrese el primer numero")
nume1 = float(input())
print("ingrese el segundo numero")
nume2 = float(input())

resultado = "no son diferentes"
#proceso
if nume1!=nume2:
    resultado = "son diferentes. la suma es", (nume1+nume2)

#salida
print(resultado)