"""
Condicionales if:
    Evaluan expresiones booleanas

Estructura:
    if expresion:
        instrucciones

    if expresion:
        instrucciones
    else:
        instrucciones
    
    if expresion:
        instrucciones
    elif expresion:
        instrucciones
    else:
        instrucciones
"""
print("Programa que verifica si un número es par")
num = int(input("Ingeresa un número: "))
if num % 2 == 0:
    print("Es un número par")
else:
    print("Es un número impar")