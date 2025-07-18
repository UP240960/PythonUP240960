#sets
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Ejercicio 1
st_age = set(age)
len_st = len(st_age)
len_ls = len(age)
igual = len_ls == len_st
mayor = len_st > len_ls
menor = len_st < len_ls
print(f'set: {len_st}\nlist: {len_ls}\n{len_st} = {len_ls} == {igual}\n{len_st} > {len_ls} == {mayor}\n{len_st} < {len_ls} == {menor}')

#Ejercicio 2
print('La diferencia entre los tipos de informacion es:\nString: Secuencia de caracteres.\nList: Una coleccion ordenada y modificable.\nTuple: Una coleccion ordenada y no modificable.\nSet: Una coleccion sin orden y de elementos unicos.')

#Ejercicio 3
oracion = "I am a teacher and I love to inspire and teach people"
palabras = oracion.split()
st_oracion = set(palabras)
print(oracion)
print(st_oracion)