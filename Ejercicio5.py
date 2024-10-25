"""
Ejercicio 5:
    Crea un programa que pida un nombre de usuario y una contraseña 
    y si se ha introducido "Fer" y "churros" se indica "Has entrado al sistema", 
    sino se da un error.
"""
usuario = input ("Ingresa tu Usuario: ")
contrasena = input ("Ingresa tu Contraseña: ")
if usuario == "Fer" and contrasena == "churros":
    print ("Has entrado al sistema")
else:
    print ("Contraseña o usuario incorrectos.")