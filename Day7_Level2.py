# sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

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
disjoin = A.isdisjoint(B)
print(disjoin)
#Ejercicio 5
A.union(B)
B.union(A)
print(A)
print(B)
#Ejercicio 6
simetrico = A.symmetric_difference(B)
print(simetrico)
#Ejercicio 7
del A
del B