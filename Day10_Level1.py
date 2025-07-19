#Ejercicio 1
for i in range(11):
    print(i)

contador = 0
while contador <= 10: 
    print(contador)
    contador += 1 

#Ejercicio 2
for i in range(10, -1, -1):
    print(i)

contador = 10  
while contador >= 0: 
    print(contador)
    contador -= 1 

#Ejercicio 3
for i in range(1, 8):
    print('#' * i)

#Ejercicio 4
for _ in range(8):
    for _ in range(7):
        print(' #', end='')
    print(' #') 

#Ejercicio 5
for i in range(11):
    resultado = i * i
    print(f"{i} x {i} = {resultado}")

#Ejercicio 6
tec = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']

for item in tec:
    print(item)

#Ejercicio 7
for numero in range(0, 101, 2):
    print(numero)

#Ejercicio 8
for numero in range(1, 101, 2):
    print(numero)