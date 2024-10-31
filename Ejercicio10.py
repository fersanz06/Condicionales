"""
Ejercicio 10:
    El director de una escuela está organizando un viaje de estudios, y requiere 
    determinar cuánto debe cobrar a cada alumno y cuánto debe pagar a la compañía de 
    viajes por el servicio. La forma de cobrar es la siguiente: 
    si son 100 alumnos o más, el costo por cada alumno es de 65 euros; 
    de 50 a 99 alumnos, el costo es de 70 euros, de 30 a 49 es de 95 euros, 
    y si son menos de 30, el costo de la renta del autobús es de 4000 euros, 
    sin importar el número de alumnos. 
    Realice un programa que permita determinar el pago a la compañía de autobuses 
    y lo que debe pagar cada alumno por el viaje.
"""
alumnos = int (input("Ingresa la cantidad de alumnos: "))
if alumnos >= 100:
    costo = (alumnos * 65)
    print (f"Cada alumno deberá pagar 65 euros y se le pagarán {costo} euros a la compañía")
elif alumnos >= 50:
    costo = (alumnos * 70)
    print (f"Cada alumno deberá pagar 70 euros y se le pagarán {costo} euros a la compañía")
elif alumnos >= 30:
    costo = (alumnos * 95)
    print (f"Cada alumno deberá pagar 95 euros y se le pagarán {costo} euros a la compañía")
else:
    costo = (4000 / alumnos)
    print (f"Cada alumno deberá pagar {costo} euros y se le pagarán 4,000 euros a la compañía")