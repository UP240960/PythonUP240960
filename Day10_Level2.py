#Ejercicio 1
total_suma = 0 

for numero in range(101): 
    total_suma += numero 

print(f"La suma de todos los números es {total_suma}.")

#Ejercicio 2
suma_pares = 0
suma_impares = 0

for numero in range(101):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(f"La suma de todos los pares es {suma_pares}.")
print(f"La suma de todos los impares es {suma_impares}.")

