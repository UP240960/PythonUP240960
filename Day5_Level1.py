#Ejercicio 1
lista = []
#Ejercicio 2
abc = ["a" , "b" , "c" , "d" , "e"]
#Ejercicio 3
print("Lista #1: " , len(lista))
print("Lista #2 :" , len(abc))
#Ejercicio 4
print("Primer item:", abc[0], "\nItem intermedio:", abc[len(abc) // 2],"\nUltimo item", abc[-1])
#Ejercicio 5
mixed_data_types = ["Alan", 23 , 1.87 , "Single" , "Buenaventura #520, col. Puentes"]
#Ejercicio 6
it_companies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]
#Ejercicio 7
print(it_companies)
#Ejercicio 8
print(len(it_companies))
#Ejercicio 9
print("Primer compañia: " , it_companies[0] , "\nCompañia de en medio: " , it_companies[len(it_companies) // 2] , "\nUltima compañia: " , it_companies[-1])
#Ejercicio 10
it_companies[0] = "Nintendo"
print(it_companies)
#Ejercicio 11
it_companies.append("Netflix")
print(it_companies)
#Ejercicio 12
it_companies.insert(len(it_companies)//2, "Samsung")
print(it_companies)
#Ejercicio 13
g=it_companies[1].upper()
it_companies[1]=g
print(it_companies)
#Ejercicio 14
separador = " #; "
companies = separador.join(it_companies)
print(companies)
#Ejercicio 15
print("Oracle" in it_companies)
#Ejercicio 16
it_companies.sort()
print(it_companies)
#Ejercicio 17
it_companies.reverse()
print(it_companies)
#Ejercicio 18
print(it_companies[0:3])
#Ejercicio 19
print(it_companies[6:])
#Ejercicio 20
print(it_companies[len(it_companies) // 2])
#Ejercicio 21
it_companies.remove(it_companies[0])
print(it_companies)
#Ejercicio 22
list_start= len(it_companies) // 2
list_end= len(it_companies) // 2 + 1
new_list= it_companies[ : list_start]+ it_companies[ list_end : ]
print(f"{new_list}")
it_companies.remove(it_companies[list_start])
print(it_companies)
#ejercicio 23
print(it_companies.remove(it_companies[]))

