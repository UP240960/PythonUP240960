#Ejercicio 1
import random
import string

def list_of_hexa_colors(num_colors):

    caracteres_hexa = string.digits + 'abcdef'
    
    colores_generados = []
    
    for _ in range(num_colors):
        codigo_hexa = ''.join(random.choice(caracteres_hexa) for _ in range(6))
        
        colores_generados.append(f"#{codigo_hexa}")
        
    return colores_generados

print("--- Generando 1 color hexadecimal ---")
print(list_of_hexa_colors(1))

print("\n--- Generando 3 colores hexadecimales ---")
print(list_of_hexa_colors(3))

print("\n--- Generando 5 colores hexadecimales ---")
print(list_of_hexa_colors(5))

#Ejercicio 2
def list_of_rgb_colors(num_colors):

    colores_generados = []

    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        colores_generados.append(f"rgb({r},{g},{b})")
    return colores_generados

print(list_of_rgb_colors(1))
print(list_of_rgb_colors(3))
print(list_of_rgb_colors(5))

#Ejercicio 3
def generate_colors(color_type, num_colors):
    
    colores_generados = []

    if not isinstance(num_colors, int) or num_colors <= 0:
        return "Error: El número de colores debe ser un entero positivo."
    
    if color_type == 'hexa':
        caracteres_hexa = string.digits + 'abcdef'
        for _ in range(num_colors):
            codigo_hexa = ''.join(random.choice(caracteres_hexa) for _ in range(6))
            colores_generados.append(f"#{codigo_hexa}")

    elif color_type == 'rgb':
        for _ in range(num_colors):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colores_generados.append(f"rgb({r}, {g}, {b})")

    else:
        return "Tipo de color inválido. Usa 'hexa' o 'rgb'."
        
    return colores_generados

print("Colores Hexa (3):", generate_colors('hexa', 3))
print("Colores Hexa (1):", generate_colors('hexa', 1))
print("Colores RGB (3):", generate_colors('rgb', 3))
print("Colores RGB (1):", generate_colors('rgb', 1))
