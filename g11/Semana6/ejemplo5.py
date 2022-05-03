#determinar si una persona es mayor de edad o menor de edad

#entrada
print("ingrese la edad:")
edad = int(input())

#proceso
if edad>=18:
    rpta = "usted es mayor de edad"#verdadero
else:
    rpta = "usted es menor de edad"#falso

#salida
print(rpta)