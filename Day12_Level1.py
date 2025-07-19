#Ejercicio 1
import random
import string

def random_user_id():

    caracteres = string.ascii_lowercase + string.digits

    random_id = ''.join(random.choice(caracteres) for i in range(6))
    return random_id

print(random_user_id())

#Ejercicio 2
def user_id_gen_by_user():
    """
    Genera un número específico de IDs de usuario aleatorios,
    cada uno con una longitud especificada por el usuario.
    Los IDs pueden contener dígitos (0-9) y letras minúsculas (a-z).
    """
    num_chars_str = input("Introduce el número de caracteres para cada ID: ")
    num_ids_str = input("Introduce la cantidad de IDs a generar: ")

    try:
        num_chars = int(num_chars_str)
        num_ids = int(num_ids_str)
    except ValueError:
        return "Entrada inválida. Por favor, introduce números enteros."

    if num_chars <= 0 or num_ids <= 0:
        return "Tanto el número de caracteres como la cantidad de IDs deben ser positivos."

    caracteres = string.ascii_lowercase + string.digits

    ids_generados = []
    for _ in range(num_ids):
        random_id = ''.join(random.choice(caracteres) for _ in range(num_chars))
        ids_generados.append(random_id)

    return '\n'.join(ids_generados)


print("Ejemplo:")
print(user_id_gen_by_user())

print("\nSegundo Ejemplo:")
print(user_id_gen_by_user())

#Ejercicio 3
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())
print(rgb_color_gen())
print(rgb_color_gen())
