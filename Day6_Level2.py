#Ejercicio 1
Hermanas= ("Karla" , "Vanessa" , "Magdalena")
Hermano= ("Daniel" , )
siblings = Hermanas + Hermano
padres= ("Gloria" , "Juan")
family_members= siblings + padres
*siblings , madre, padre = family_members
print(f'Mis hermanos son: {siblings}')
print(f'mis padres son: {padre} y {madre}')
#Ejerciio 2
frutas = ('mango' , 'piña' , 'sandia')
print(f'frutas: {frutas}')
vegetales = ('pepino' , 'cebolla' , 'aguacate')
print(f'verduras: {vegetales}')
comida_animal = ('leche' , 'huevo' , 'carne')
print(f'comida de  origen animal: {comida_animal}')
tupla_comida= frutas + vegetales + comida_animal
print(f'tupla: {tupla_comida}')
#Ejercicio 3
lista_comida = list(tupla_comida)
print(f'lista: {lista_comida}')
#Ejercicio 4
medio = len(lista_comida) //2
comida = lista_comida[medio]
print(f'El mediode es: {comida}')
#Ejercicio 5
primeros = lista_comida[ : 3]
ultimos = lista_comida[-3 : ]
print(f'Los primerso son: {primeros}')
print(f'Los ultimos son: {ultimos}')
#Ejercicio 6
del tupla_comida
#Ejercicio 7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
#Punto 1
estonia = 'Estonia' in nordic_countries
print(f'Estonia es un pais nordico: {estonia}')
#Punto 2
islandia = 'Iceland' in nordic_countries
print(f'Islandia es un pais nordico: {islandia}')