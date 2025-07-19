#Ejercicio 1
def evens_and_odds(number):
    if not isinstance(number, int) or number < 0:
        return "Error: Por favor, introduce un número entero positivo."
    
    count_evens = 0
    count_odds = 0

    for i in range(number + 1):
        if i % 2 == 0:
            count_evens += 1
        else:
            count_odds += 1

    return f"El número de impares son {count_odds}.\nEl número de pares son {count_evens}."

print(evens_and_odds(100))

#Ejercicio 2
def factorial(n):
    if not isinstance(n, int):
        return "Error: La entrada debe ser un número entero."
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    if n == 0:
        return 1
    res = 1
    for i in range(1, n + 1):
        res *= i # res = res * i
    return res

print(f"El factorial de 2 es: {factorial(2)}")
print(f"El factorial de 5 es: {factorial(5)}")

#Ejercicio 3
def is_empty(data):
    return not bool(data)

print(f"¿'': {is_empty('')}")

#Ejercicio 4
import math
from collections import Counter

def validate_numeric_list(data):
    if not isinstance(data, list):
        raise TypeError("La entrada debe ser una lista.")
    if not data:
        raise ValueError("La lista no puede estar vacía.")
    for item in data:
        if not isinstance(item, (int, float)):
            raise TypeError("Todos los elementos de la lista deben ser números (enteros o flotantes).")
    return True

def calculate_mean(data):
    try:
        validate_numeric_list(data)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

    return sum(data) / len(data)

def calculate_median(data):
    try:
        validate_numeric_list(data)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

    sorted_data = sorted(data)
    n = len(sorted_data)

    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
         mid1 = sorted_data[n // 2 - 1]
         mid2 = sorted_data[n // 2]
    return (mid1 + mid2) / 2

def calculate_mode(data):
    try:
        validate_numeric_list(data)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"
    counts = Counter(data)
    if not counts:
        return []
    max_count = 0
    if counts:
        max_count = max(counts.values())
    modes = [key for key, value in counts.items() if value == max_count]
    if max_count == 1 and len(modes) == len(data):
        return "No hay una moda clara (todos los elementos aparecen una vez)."
    return modes

def calculate_range(data):
    try:
        validate_numeric_list(data)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

    return max(data) - min(data)

def calculate_variance(data, sample=True):

    try:
        validate_numeric_list(data)
    except (TypeError, ValueError) as e:
        return f"Error: {e}"

    n = len(data)
    if sample and n < 2:
        return "Error: Para la varianza muestral, la lista debe contener al menos dos elementos."
    if not sample and n < 1:
        return "Error: Para la varianza poblacional, la lista no puede estar vacía."

    mean = calculate_mean(data)
    if isinstance(mean, str) and mean.startswith("Error"):
        return mean
    squared_differences_sum = sum((x - mean) ** 2 for x in data)
    # Denominador basado en si es varianza muestral o poblacional
    denominator = (n - 1) if sample else n

    return squared_differences_sum / denominator

def calculate_std(data, sample=True):
    variance = calculate_variance(data, sample)
    if isinstance(variance, str) and variance.startswith("Error"): # Propagar error de la varianza
        return variance
    
    return math.sqrt(variance)

print('Ejemplo')
data1 = [1, 2, 3, 4, 5]
print(f"\nDatos: {data1}")
print(f"Media: {calculate_mean(data1)}")
print(f"Mediana: {calculate_median(data1)}")
print(f"Moda: {calculate_mode(data1)}")
print(f"Rango: {calculate_range(data1)}")
print(f"Varianza (muestral): {calculate_variance(data1)}")
print(f"Desviación Estándar (muestral): {calculate_std(data1)}")
