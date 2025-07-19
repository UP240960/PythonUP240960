#Ejercicio 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number <= 0]
print(negative_and_zero)

#Ejercicio 2
lista_de_lista = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_lista = [item for sublista1 in lista_de_lista for sublista2 in sublista1 for item in sublista2]

print(flattened_lista)

#Ejercicio 3
resultado_lista = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(resultado_lista)

#Ejercicio 4
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

paisses_transfromados = [
    [country.upper(), country.upper()[:3], capital.upper()]
    for sublista in paises
    for country, capital in sublista
]

print(paisses_transfromados)

#Ejercicio 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

list_of_dictionaries = [
    {'country': country.upper(), 'city': capital.upper()}
    for sublist in countries
    for country, capital in sublist
]

print(list_of_dictionaries)

#Ejercicio 6
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

nombres_completos = [
    f"{nombre} {apellido}"
    for sublista in nombres
    for nombre, apellido in sublista
]

print(nombres_completos)

#Ejercicio 7
calcular_pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else "Indefinida (línea vertical)"

m1 = calcular_pendiente(1, 2, 3, 4)
print(f"Pendiente entre (1,2) y (3,4): {m1}")

m2 = calcular_pendiente(0, 0, 5, 10)
print(f"Pendiente entre (0,0) y (5,10): {m2}")

m3 = calcular_pendiente(2, 1, 2, 5)
print(f"Pendiente entre (2,1) y (2,5): {m3}")