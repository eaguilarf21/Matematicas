#Ingresar el sueldo de un empleado y de acuerdo a su categoria se le darà
# una bonificacion:
#si la categoria es "a" se le darà un bono del 5%
#si la categoria es "b" se le darà un bono del 10%
#si la categoria es "c" se le darà un bono del 15%
#calcule la bonificacion y el sueldo neto

#
print("ingrese el sueldo")
sueldo = float(input())

print("ingrese la categoria en minusculas")
cat = input()

#
if cat=="a" or cat =="A":
    bonif = 5/100*sueldo
elif cat=="b" or cat == "B":
    bonif = 10/100*sueldo
elif cat=="c" or cat =="C":
    bonif = 15/100*sueldo
else:
    bonif= 0

sueldoneto = sueldo+bonif

#
print("la bonificacion es de :",bonif)
print("el sueldo neto es :",sueldoneto)