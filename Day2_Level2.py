#variables
first_name="Alan"
last_name="Jauregui"
full_name="Alan Jauregui"
country="Mexico"
city="Aguascalientes"
age="23"
year="2025"
is_married= "Single"
is_true=True
is_light_on=False
A, B, C= 2, 5, 0
#Usando type()
print("variable primer nombre")
print(type(first_name))
print("Variable apellido")
print(type(last_name))
print("Variable nombre completo")
print(type(full_name))
print("Variable pais")
print(type(country))
print("Variable ciudad")
print(type(city))
print("Variable edad")
print(type(age))
print(type(year))
print("Varibable año")
print(type(year))
print("Variable estado fiscal")
print(type(is_married))
print("Variable es verdadero")
print(type(is_true))
print("Variable luz")
print(type(is_light_on))
print("Multiples variables")
print(type(A),type(B),type(C))
#Usando Len()
print(len(first_name))
print(len(last_name))
print("Primer nombre = ", len(first_name)," Apellido = ", len(last_name))
#Declarar Operaciones
num_one=5 
num_two=4
total= num_one + num_two
print(num_one, "+", num_two, "=", total)
diff=num_one-num_two
print(num_one,"-", num_two, "=", diff)
product= num_one * num_two
print(num_one, "*", num_two, "=", product)
division= num_one / num_two
print(num_one, "/", num_two, "=", division)
remainder= num_one % num_two
print( num_one, "%", num_two, "=", remainder)
exp= num_one ** num_two
print(num_one, "**", num_two, "=", exp)
floor_division= num_one // num_two
print(num_one, " // ", num_two, "=", floor_division)
import math
radius=30
area_of_circle= math.pi * radius ** 2
circum_of_circle= 2 * math.pi * radius
print("El radio es de", radius)
print("El area de un ciruclo es de", area_of_circle)
print("La circunferencia", circum_of_circle)
user_radius = float(input("Enter radius to calculate area: "))
user_area = math.pi * user_radius ** 2
print("Area basado en el user imput:", user_area)
first_name= input("Ingresa tu primer nombre")
last_name= input("Ingresa tu apellido")
country= input("Ingresa tu país")
age= input("Ingresa tu edad")
print("Primer nombre: ", first_name)
print("Apellido: ", last_name)
print("Pais: ", country)
print("Edad: ", age)
help('keywords')
