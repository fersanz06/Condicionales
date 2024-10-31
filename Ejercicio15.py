"""
Ejercicio 15:
    Juego Piedra Papel y Tijera
    Programa que lea las opciones de 2 jugadores, y muestra el resultado
    Empate, gana jugador 1 o gana jugador 2
    Si introducimos una opción que no coindica con piedra, papel o tijera
    Diga que opción Incorrecta
"""
jugador_1 = input ("Jugador 1. piedra, papel o tijeras: ")
jugador_2 = input ("Jugador 2. piedra, papel o tijeras: ")
if jugador_1 == "piedra" and jugador_2 == "piedra":
    print ("Empate")
elif jugador_1 == "papel" and jugador_2 == "papel":
    print ("Empate")
elif jugador_1 == "tijeras" and jugador_2 == "tijeras":
    print ("Empate")
elif jugador_1 == "papel" and jugador_2 == "piedra":
    print ("Gana jugador 1")
elif jugador_1 == "tijeras" and jugador_2 == "papel":
    print ("Gana jugador 1")
elif jugador_1 == "piedra" and jugador_2 == "tijeras":
    print ("Gana jugador 1")
elif jugador_2 == "papel" and jugador_1 == "piedra":
    print ("Gana jugador 2")
elif jugador_2 == "tijeras" and jugador_1 == "papel":
    print ("Gana jugador 2")
elif jugador_2 == "piedra" and jugador_1 == "tijeras":
    print ("Gana jugador 2")
else:
    print ("Error")