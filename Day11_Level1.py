#Ejercicio 1
def add_two_numbers(num1, num2):
    return num1 + num2

print('Ejemplo')
print(f"La suma de 5 y 3 es: {add_two_numbers(5, 3)}")

#Ejercicio 2
import math

def area_of_circle(radius):
    if not isinstance(radius, (int, float)):
        return "Error: El radio debe ser un número (entero o flotante)."
    if radius < 0:
        return "Error: El radio no puede ser un número negativo."
    area = math.pi * radius * radius
    return area

print('Ejemplo')
radio1 = 5
area1 = area_of_circle(radio1)
print(f"El área de un círculo con radio {radio1} es: {area1:.2f}")

#Ejercicio 3
def add_all_nums(*args):
    total_sum = 0

    for arg in args:
        if not isinstance(arg, (int, float)):
            return f"Error: Todos los argumentos deben ser números. Se encontró un argumento de tipo '{type(arg).__name__}' con valor '{arg}'."
        total_sum += arg
    return total_sum

print('Ejemplo')
print(f"Suma de (1, 2, 3): {add_all_nums(1, 2, 3)}")

#Ejercicio 4
def convert_celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        return "Error: La temperatura en Celsius debe ser un número (entero o flotante)."
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print('Ejemplo')
temp_c2 = 37
temp_f2 = convert_celsius_to_fahrenheit(temp_c2)
print(f"{temp_c2}°C es igual a {temp_f2:.2f}°F")

#Ejercicio 5
def check_season(month):
    month_lower = month.lower()
    if month_lower in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif month_lower in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif month_lower in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif month_lower in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return "Error: Mes inválido. Por favor, introduce un nombre de mes válido en español."

print('Ejemplo')
print(f"La estación en 'mayo' es: {check_season('mayo')}")

#Ejercicio 6
def calculate_slope(x1, y1, x2, y2):
    if not all(isinstance(arg, (int, float)) for arg in [x1, y1, x2, y2]):
        return "Error: Todas las coordenadas deben ser números (enteros o flotantes)."
    if x2 - x1 == 0:
        return "Pendiente indefinida (línea vertical)"
    slope = (y2 - y1) / (x2 - x1)
    return slope

print('Ejemplo')
print(f"Pendiente entre (1, 2) y (3, 4): {calculate_slope(1, 2, 3, 4)}")

#Ejercicio 7
def solve_quadratic_eqn(a, b, c):
    if not all(isinstance(arg, (int, float)) for arg in [a, b, c]):
        return "Error: Los coeficientes (a, b, c) deben ser números."
    if a == 0:
        if b == 0:
            if c == 0:
                return "Infinitas soluciones (0 = 0)"
            else:
                return "No hay solución (constante ≠ 0)"
        else:
            x = -c / b
            return (x,)
    delta = (b**2) - (4 * a * c)
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return (x1, x2)
    elif delta == 0:
        x = -b / (2 * a)
        return (x,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(delta)) / (2 * a)
        x1_complex = complex(real_part, imaginary_part)
        x2_complex = complex(real_part, -imaginary_part)
    return (x1_complex, x2_complex)

print('Ejemplo')
print(f"Ecuación x^2 + 4x + 4 = 0: {solve_quadratic_eqn(1, 4, 4)}")

#Ejercicio 8
def print_list(input_list):
    if not isinstance(input_list, list):
        print("Error: La entrada debe ser una lista.")
        return
    for item in input_list:
        print(item)
print('Ejemplo')
my_numbers = [1, 2, 3, 4, 5]
print("\nElementos de my_numbers:")
print_list(my_numbers)

##Ejercicio 9
def reverse_list(input_list):
    if not isinstance(input_list, list):
        return "Error: La entrada debe ser una lista."
    
    reversed_items = []

    for i in range(len(input_list) - 1, -1, -1):
        reversed_items.append(input_list[i])
    return reversed_items

print('Ejemplo')
print(f"Lista original: [1, 2, 3, 4, 5]")
print(f"Lista invertida: {reverse_list([1, 2, 3, 4, 5])}")
print(f"Lista original: ['A', 'B', 'C']")
print(f"Lista invertida: {reverse_list(['A', 'B', 'C'])}")

#Ejercicio 10
def capitalize_list_items(input_list):
    if not isinstance(input_list, list):
        return "Error: La entrada debe ser una lista."

    capitalized_items = []

    for item in input_list:
        if isinstance(item, str):
            capitalized_items.append(item.capitalize())
        else:
            capitalized_items.append(item)
            
    return capitalized_items

print('Ejemplo')
mixed_data = ["manzana", 123, "banana", True, "cereza"]
print(f"\nLista original: {mixed_data}")
print(f"Lista capitalizada: {capitalize_list_items(mixed_data)}")

#Ejercicio 11
def add_item(input_list, item_to_add):
    if not isinstance(input_list, list):
        return "Error: La primera entrada debe ser una lista."
    new_list = list(input_list)
    new_list.append(item_to_add)

    return new_list

print('\nEjemplo')
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"\nLista original: {food_staff}")
new_food_staff = add_item(food_staff, 'Meat')
print(f"Lista con 'Meat' añadido: {new_food_staff}")
print(f"La lista original no se modificó: {food_staff}")
numbers = [2, 3, 7, 9]
print(f"\nLista original: {numbers}")
new_numbers = add_item(numbers, 5)
print(f"Lista con 5 añadido: {new_numbers}")
print(f"La lista original no se modificó: {numbers}")

#Ejercicio 12
def remove_item(input_list, item_to_remove):
    if not isinstance(input_list, list):
        return "Error: La primera entrada debe ser una lista."
    new_list = list(input_list) 

    try:
        new_list.remove(item_to_remove)
    except ValueError:
        pass

    return new_list

print('\nEjemplo')
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(f"\nLista original: {food_staff}")
new_food_staff = remove_item(food_staff, 'Mango')
print(f"Lista sin 'Mango': {new_food_staff}")
print(f"La lista original no se modificó: {food_staff}")
numbers = [2, 3, 7, 9]
print(f"\nLista original: {numbers}")
new_numbers = remove_item(numbers, 3)
print(f"Lista sin 3: {new_numbers}")
print(f"La lista original no se modificó: {numbers}")

#Ejercicio 13
def sum_of_numbers(limit):
    if not isinstance(limit, int):
        return "Error: El parámetro 'limit' debe ser un número entero."
    if limit < 0:
        return "Error: El 'limit' no puede ser un número negativo."
    total_sum = 0
    for num in range(limit + 1):
        total_sum += num
        return total_sum

print('\nEjemplo')
print(f"Suma hasta 5: {sum_of_numbers(5)}")
print(f"Suma hasta 10: {sum_of_numbers(10)}")
print(f"Suma hasta 100: {sum_of_numbers(100)}")

#Ejercicio 14
def sum_of_odds(limit):
    if not isinstance(limit, int):
        return "Error: El parámetro 'limit' debe ser un número entero."
    if limit < 0:
        return "Error: El 'limit' no puede ser un número negativo."
    
    total_odd_sum = 0

    for num in range(limit + 1):
        if num % 2 != 0: 
            total_odd_sum += num
            return total_odd_sum
print('\nEjemplo')
print(f"Suma de impares hasta 5: {sum_of_odds(5)}")

#Ejercicio 15
def sum_of_even(limit):
    if not isinstance(limit, int):
        return "Error: El parámetro 'limit' debe ser un número entero."
    if limit < 0:
        return "Error: El 'limit' no puede ser un número negativo."
    total_even_sum = 0
    for num in range(limit + 1):
        if num % 2 == 0: 
            total_even_sum += num
    return total_even_sum

print('\nEjemplo')
print(f"Suma de pares hasta 10: {sum_of_even(10)}")
