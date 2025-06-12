#Ejercicio 1
#interger
age= 23
#Ejercicio 2
#float
height= 1.87
#Ejercicio 3
#numero complejo
complex_num= 2+2j
#Ejercicio 4
base = float(input("Base del triángulo: "))
height_tri = float(input("Altura del triángulo: "))
triangle_area = 0.5 * base * height_tri
print("El area del triángulo es:", triangle_area)
#Ejercicio 5
a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))
perimeter = a + b + c
print("El perimetro es ", perimeter)
#Ejercicio 6
length = float(input("Lado: "))
width = float(input("Ancho: "))
rect_area = length * width
rect_perimeter = 2 * (length + width)
print("Area del rectángulo:", rect_area)
print("Perimetro del rectángulo:", rect_perimeter)
#Ejercicio 7
radius = float(input("Radio del circulo: "))
circle_area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("Area de circulo:", circle_area)
print("Circumferencia del circulo:", circumference)
#Ejercicio 8
m = 2
b = -2
y_interseccion = b
x_interseccion = -b / m
print("Ecuación: y = 2x - 2")
print("Pendiente (slope):", m)
print("Intersección en Y (y-intercept):", y_interseccion)
print("Intersección en X (x-intercept):", x_interseccion)
#Ejercicio 9
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)
print("Punto 1: (", x1, ",", y1, ")")
print("Punto 2: (", x2, ",", y2, ")")
print("Pendiente (slope):", pendiente)
print("Distancia euclidiana:", distancia)
#Ejercicio 10
print("Pendiente en tarea 8:", m)
print("Pendiente en tarea 9:", pendiente)
if m == pendiente:
    print("Las pendientes son iguales.")
else:
    print("Las pendientes son diferentes.")
#Ejercicio 11
print(" x\t|\ty")
print("---------------------")
for x in range(-10, 5):
    y = x**2 + 6*x + 9
    print(f"{x}\t|\t{y}")
    if y == 0:
        print(f" es igual a 0 cuando x = {x}")
#Ejercicio 12
palabra1 = "python"
palabra2 = "dragon"
longitud1 = len(palabra1)
longitud2 = len(palabra2)
print(f"Longitud de '{palabra1}':", longitud1)
print(f"Longitud de '{palabra2}':", longitud2)
comparacion_falsa = longitud1 != longitud2
print("¿Las longitudes son diferentes?", comparacion_falsa)
#Ejercicio 13
resultado = 'on' in palabra1 and 'on' in palabra2
print("¿'on' está en ambas palabras?", resultado)
#Ejercicio 14
oracion = "I hope this course is not full of jargon."
contiene_jargon = "jargon" in oracion
print("¿La palabra 'jargon' está en la oración?", contiene_jargon)
#Ejercicio 15
no_esta_en_ambas = 'on' not in palabra1 and 'on' not in palabra2

print("¿No hay 'on' en ambas palabras?", no_esta_en_ambas)
#Ejercicio 16
texto = "python"
longitud = len(texto)
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print("Longitud original (int):", longitud)
print("Longitud como float:", longitud_float)
print("Longitud como string:", longitud_str)
#Ejercicio 17
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print(f"{numero} es un número par.")
else:
    print(f"{numero} es un número impar.")
#Ejercicio 18
floor_div = 7 // 3
int_value = int(2.7)
resultado = floor_div == int_value
print("Floor division 7 // 3:", floor_div)
print("int(2.7):", int_value)
print("¿Son iguales?", resultado)
#Ejercicio 19
tipo_cadena = type('10')
tipo_entero = type(10)
son_iguales = tipo_cadena == tipo_entero
print("Tipo de '10':", tipo_cadena)
print("Tipo de 10:", tipo_entero)
print("¿Son iguales?", son_iguales)
#Ejercicio 20
valor = int(float('9.8'))
comparacion = valor == 10
print("Valor convertido:", valor)
print("¿Es igual a 10?", comparacion)
#Ejercicio 21
horas = float(input("Enter hours: "))
tarifa = float(input("Enter rate per hour: "))
pago = horas * tarifa
print("Your weekly earning is", pago)
#Ejercicio 22
años_vividos = int(input("Enter number of years you have lived: "))
segundos_por_año = 365 * 24 * 60 * 60  # 365 días * 24 horas * 60 minutos * 60 segundos
segundos_vividos = años_vividos * segundos_por_año
print(f"You have lived for {segundos_vividos} seconds.")
#Ejercicio 23
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
