#Ejercicio 1
thirty="Thirty "
days="Days "
of="of "
python="Python"
all_text= thirty + days + of + python
print(thirty)
print(days)
print(of)
print(python)
print(all_text)
#Ejercicio 2
coding="Coding "
For="For "
all="All "
text= coding + For + all
print(coding)
print(all)
print(text)
#Ejercicio 3
company= "Coding For All"
#Ejercicio 4
print(company)
#Ejercicio 5
print(len(company))
#Ejercicio 6
print(company.upper())
#Ejercicio 7
print(company.lower())
#Ejercicio 8
print(company.capitalize())
print(company.title())
print(company.swapcase())
#Ejercicio 9
find_text= company.find(" ")
slice_text= company[find_text+1:]
print(slice_text)
#Ejercicio 10
print(company.index("Coding") !=-1)
#Ejercicio 11
company2=company.replace("Coding", "Python")
print(company2)
#Ejercicio 12
company3=company2.replace("Python", "Everyone")
print(company3)
#Ejercicio 13
print(company.split())
#Ejercicio 14
list_companies= "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(list_companies.split())
#Ejercicio 15
print("El primer caracter es:", company[0])
#Ejercicio 16
print("El ultimo caracter es:", company[-1])
#Ejercicio 17
print("El caracter 10 es:", company[10])
#Ejercicio 18
print('El acronimo para "Coding For All" es ',"".join(palabra[0] for palabra in company.split()))
#Ejercicio 19
print('El acronimo de "Python for all"', "".join(palabra[0] for palabra in company2.split()))
#Ejercicio 20
print('La posición de "C" es: ', company.index("C"))
#Ejercicio 21
print('La posicionde "F" es: ', company.index("F"))
#Ejercicio 22
cfap= "Coding For All People"
print("La ultima vez que l  aparece es en la posición: ", cfap.rfind("l"))
#Ejercicio 23
sentence= 'You cannot end a sentence with "because", because "because" is a conjunction'
print('La primera vez que aparece la palabra "because" es en: ', sentence.index("because"))
#Ejercicio 24
print('La ultima vez que la palabra "because" es en:', sentence.rindex("because"))
#Ejercicio 25
becuase= '"because", because "because"'
print(sentence.replace(becuase,"").strip())
#Ejercicio 26
print('La primera vez que "because" aparece es en:', sentence.find("because"))
#Ejercicio 27
print(sentence.replace(becuase,"").strip())
#Ejercicio 28
print(company.startswith("Coding"))
#Ejercicio 29
print(company.endswith("coding"))
#Ejercicio 30
espacios="  Coding For All   "
print(espacios.strip())
#Ejercicio 31
DP= "30DaysOfPython"
TDP= "thirty_days_of_python"
print(DP.isidentifier())
print(TDP.isidentifier())
#Ejercicio 32
names=["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
print("#".join(names))
print(" ".join(names))
#Ejercicio 33
print("I am enjoying this challege.\nI jsut wonder what is next")
#Ejercicio 34
print("Name\tAge\tCountry\tCity")
print("Asbeneh\t250\tFinland\tHelsinki")
#Ejercicio 35
radius = 10
area = 3.14 * radius ** 2
print("radio = ", radius)
print("area = ", area)
print(f"El area de un circulo con un radio de {radius}, es {int(area)} metros cuadrados")
#Ejercicio 36
num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")
print(f"{num1} % {num2} = {num1 % num2}")
print(f"{num1} // {num2} = {num1 // num2}")
print(f"{num1} ** {num2} = {num1 ** num2}")
