#Ejercicio 1
puntuacion = float(input("Introduce la puntuación del estudiante (0-100): "))

if 80 <= puntuacion <= 100:
    print("Calificación: A")
elif 70 <= puntuacion < 80:
    print("Calificación: B")
elif 60 <= puntuacion < 70:
    print("Calificación: C")
elif 50 <= puntuacion < 60:
    print("Calificación: D")
elif 0 <= puntuacion < 50:
    print("Calificación: F")
else:
    print("Puntuación inválida. Por favor, introduce un número entre 0 y 100.")

#Ejercicio 2
mes = input("Introduce un mes del año").strip().lower()

if mes in ["septiembre", "octubre", "noviembre"]:
    print("La estación es Otoño.")
elif mes in ["diciembre", "enero", "febrero"]:
    print("La estación es Invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("La estación es Primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("La estación es Verano.")
else:
    print("Mes no reconocido. Por favor, asegúrate de escribir el mes correctamente.")

#Ejercicio 3
frutas = ['lima', 'guayaba', 'mango', 'limon']

fruta_añadida = input("Introduce una fruta para añadir: ").strip().lower()

if fruta_añadida in frutas:
    print('Esa fruta ya existe en la lista.')
else:
    frutas.append(fruta_añadida)
    print(f"La fruta '{fruta_añadida}' ha sido añadida.")
    print("Lista de frutas actualizada:", frutas)