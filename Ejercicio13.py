"""
Ejercicio 13:
    Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba 
    el dí­a correspondiente. 
    Si introducimos otro número nos da un error.
"""
dia = int (input ("Ingresa un día de la semana de 1 al 7: "))
if dia >= 8:
    print ("Error")
elif dia == 2:
    print ("Lunes")
elif dia == 3:
    print ("Martes")
elif dia == 4:
    print("Miércoles")
elif dia == 5:
    print ("Jueves")
elif dia == 6:
    print ("Viernes")
elif dia == 7:
    print ("Sábado")
else:
    print ("Domingo")