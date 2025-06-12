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
print("El acronimo para (coding for all) es ","".join(palabra[0] for palabra in company.split()))
#Ejercicio 19
print("El acronimo de (Python for all)", "".join(palabra[0] for palabra in company2.split()))
#Ejercicio 20
