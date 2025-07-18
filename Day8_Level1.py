#Ejercicio 1
dog = {}

#Ejercicio 2
dog["Nombre"] = "Apolo"
dog["Color"] = "Amarillo"
dog["Raza"] = "Golden Retriever"
dog["Patas"] = 4
dog["Años"] = 2
print(dog)

#Ejercicio 3
estudiante = {'Nombre':'Lana' , 'Apellido': 'Castillo' , 'Genero':'Mujer' , 'Años':13 , 'Estado Civil':'Soltera' , 'Habilidades':['Deportivas' , 'Artisticas'] , 'País':'España' , 'Ciudad':'Madrid' , 'Direccion':'calle123 #ABC, Colonia *******'}

#Ejercicio 4
largo = len(estudiante)
print(largo)

#Ejercicio 5
skills = estudiante['Habilidades']
print(type(skills))

#Ejercicio 6
estudiante['Habilidades'].append('Matematicas')
print(estudiante['Habilidades'])

#Ejercicio 7
claves = estudiante.keys()
print(claves)

#Ejercicio 8
valores = estudiante.values()
print(valores)

#Ejercicio 9
tuplas = estudiante.items()
print(tuplas)

#Ejercicio 10
borrar = estudiante.pop('Direccion')
print(estudiante)

#Ejercico 11
del estudiante
