#Ejercicio 1
import random

def shuffle_list(my_list):
    random.shuffle(my_list)
    return my_list

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Lista original de números: {numeros}")
lista_mezclada_numeros = shuffle_list(numeros)
print(f"Lista de números mezclada: {lista_mezclada_numeros}")

#Ejercicio 2
def generate_unique_random_numbers():
    poblacion = list(range(10))
    numeros_unicos = random.sample(poblacion, 7)
    
    return numeros_unicos

print(generate_unique_random_numbers())
