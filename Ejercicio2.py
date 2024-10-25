"""
Ejercicio 2:
    Crea un programa que pida un número y diga si es positivo, negativo o 0.
"""
print("Programa que escribre si un número es positivo, negativo o 0")
num = int (input("Ingresa un numero: "))
if num > 0:
    print ("El número es positivo")
elif num < 0:
    print ("El número es negativo")
else:
    print ("El numero es 0")