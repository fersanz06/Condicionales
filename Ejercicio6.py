"""
Ejercicio 6:
    Crea un programa que lea una cadena por teclado y compruebe si es una letra 
    mayúscula.
"""
cadena = input ("Ingresa una letra: ")
if len (cadena) == cadena.isupper():
    print ("Es una letra mayúscula")
else:
    print ("No es una letra mayúscula")