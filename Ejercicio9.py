"""
Ejercicio 9:
    Programa que pida tres números y los muestre ordenados
    (de mayor a menor)
"""
num1 = int (input("Ingresa un número: "))
num2 = int (input("Ingresa otro número: "))
num3 = int (input("Ingresa otro número: "))
if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        ordenados = (num1, num2, num3)
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        ordenados = (num2, num1, num3)
    else:
        ordenados = (num2, num3, num1)
else:
    if num1 >= num2:
        ordenados = num3, num1, num2
    else:
        ordenados = num3, num2, num1
print (f"Los números ordenados son: {ordenados}")