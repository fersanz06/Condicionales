"""
Ejercicio 14:
    Escribe un programa que pida un número entero entre uno y doce 
    e imprime el número de días que tiene el mes correspondiente. 
    Si introducimos otro número nos da un error.
"""
print ("Programa que escribe el número de días que tiene el mes correspondiente. ")
num = int (input("Ingresa un número del 1 al 12: "))
if num == 1:
    print ("Enero tiene 31 días")
elif num == 2:
    print ("Febrero tiene 28 días")
elif num == 3:
    print ("Marzo tiene 31 días")
elif num == 4:
    print ("Abril tiene 30 días")
elif num == 5:
    print ("Mayo tiene 31 días")
elif num == 6:
    print ("Junio tiene 30 días")
elif num == 7:
    print ("Julio tiene 31 días")
elif num == 8:
    print ("Agosto tiene 31 días")
elif num == 9:
    print ("septiembre tiene 30 días")
elif num == 10:
    print ("Octubre tiene 31 días")
elif num == 11:
    print ("Noviembre tiene 30 días")
elif num == 12:
    print ("Diciembre tiene 31 días")
else:
    print ("Error")