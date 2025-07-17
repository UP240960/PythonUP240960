# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
#Ejercicio 1
largo = len(it_companies)
print(f'En copañias hay: {largo} archivos')
#Ejercicio 2
it_companies.add('Twitter')
print(it_companies)
#Ejercicio 3
it_companies.update(["Netflix" , "Samsung" , "Cisco"])
print(it_companies)
#Ejercicio 4
it_companies.remove('Microsoft')
print(it_companies)
#Ejercicio 5
print('El metodo remove se usa para elementos que estas seguro queexiten en el set.\nMientras que el discard es usado para cuando no estas seguro si exite en el set.')