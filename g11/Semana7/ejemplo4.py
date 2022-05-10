#Ingresar el sueldo de un empleado y de acuerdo a su categoria
# se le darà una bonificaciòn
#cat a - 5%, cat b - 10%, cat c - 15%. Calcule la bonificaciòn
# y el sueldo neto

#entrada
print("ingrese el sueldo")
sueldo = float(input())

print("ingrese la categoria")
cat = input()

#proceso
if cat == "a":
    bono=5/100
elif cat =="b":
    bono = 10/100
elif cat =="c":
    bono = 15/100
else:
    bono = 0

bonificacion = sueldo*bono

#salida
print("la bonificacion es", bonificacion)
print("el sueldo neto es", sueldo+bonificacion)