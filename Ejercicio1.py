"""
Ejercicio 1:
    crea un programa que pida dos números e indique Cuál es el mayor
    Si los dos son iguales que muestre el mensaje "Son iguales"
"""
print("Programa que indica si un numero es mayor o si son iguales")
num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa otro número: "))
if num1>num2:
    print(f"El número {num1}es mayor")
elif num2>num1:
    print(f"El número {num2} es mayor")
else:
    print("Los números son iguales")