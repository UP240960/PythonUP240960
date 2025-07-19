#Ejercicio 1
e = int(input('Ingresa tu edad:'))
d = 18 - e

if  e >= 18:
    print(f'Eres lo suficiente mente mayor para manejar')
if e < 18:
    print(f'Te faltan {d} años para poder manejar')

#Ejercicio 2
a = int(input("Introduce tu edad: "))
m = 23

if a > m:
    diferencia = a - m
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif m > a:
    diferencia = m - a
    if diferencia == 1:
            print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("¡Tenemos la misma edad!")

#Ejercicio 3
uno = float(input("Introduce el primer número: "))
dos = float(input("Introduce el segundo número: "))

if uno > dos:
    print(f"{uno} es mayor que {dos}")
elif uno < dos:
    print(f"{uno} es menor que {dos}")
else:
    print(f"{uno} es igual a {dos}")