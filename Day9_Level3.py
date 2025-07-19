#Ejercicio 1
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

#Punto 1
print("Verificación de skills")
if 'skills' in person:
    skills_list = person['skills']
    if skills_list:  # Asegurarse de que la lista no esté vacía
        middle_index = len(skills_list) // 2
        print(f"La habilidad del medio es: {skills_list[middle_index]}")
    else:
        print("La lista de habilidades está vacía.")
else:
    print("El diccionario 'person' no tiene la clave 'skills'.")

#Punto 2
print("\n--- Verificación de habilidad 'Python' ---")
if 'skills' in person:
    if 'Python' in person['skills']:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona NO tiene la habilidad 'Python'.")
else:
    print("El diccionario 'person' no tiene la clave 'skills'.")


#Punto 3
print("\n--- Determinación del título del desarrollador ---")
if 'skills' in person:
    skills = person['skills']
    skills_set = set(skills)

    frontend_skills = {'JavaScript', 'React'}
    backend_skills = {'Node', 'Python', 'MongoDB'}
    fullstack_skills = {'React', 'Node', 'MongoDB'}

    if skills_set.issuperset(frontend_skills) and len(skills_set) == len(frontend_skills):

        print('Es un desarrollador front-end.')
    elif skills_set.issuperset(backend_skills):
        print('Es un desarrollador back-end.')
    elif skills_set.issuperset(fullstack_skills) and 'React' in skills_set: 
        print('Es un desarrollador fullstack.')
    else:
        print('Título desconocido.')
else:
    print("El diccionario 'person' no tiene la clave 'skills', no se puede determinar el título.")


#Punto 4
print("\n--- Información personal ---")
if person.get('is_marred') and person.get('country') == 'Finland':
    first_name = person.get('first_name', 'NombreDesconocido')
    last_name = person.get('last_name', 'ApellidoDesconocido')
    country = person.get('country', 'PaísDesconocido')
    
    print(f"{first_name} {last_name} vive en {country}. Está casado/a.")
else:
    print("La persona no cumple las condiciones para imprimir la información específica (no está casada o no vive en Finlandia).")