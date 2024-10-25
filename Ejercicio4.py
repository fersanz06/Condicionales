"""
Ejercicio 4:
    Crea un programa que pida al usuario dos números y muestre su división 
    si el segundo no es cero, o un mensaje de aviso en caso contrario.
"""
num1 = int (input("Ingresa un número: "))
num2 = int (input("Ingresa otro número: "))
if num2 != 0:
    divicion = (num1 / num2)
    print (f"El resultado es {divicion}")
else:
    print ("Error, no se puede dividir entre cero")