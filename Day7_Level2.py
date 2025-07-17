# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Ejercicio 1
AB = A.union(B)
print(AB)
#Ejercicio 2
interseccion = A.intersection(B)
print(interseccion)
#Ejercicio 3
subset = A.issubset(B)
print(subset)
#Ejercicio 4
