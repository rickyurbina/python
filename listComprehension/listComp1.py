#list Comprehension
#   Sirve para crear una lista nueva a partir de una existente, cambiando los valores originales
#   Esquema general
#   newList = [newItem for item in list]

list = [1,2,3]
newList = []
for n in list:
    add_1 = n + 1
    newList.append(add_1)

print(newList)

## Aplicando List Comprehension
numbers = [1,2,3]
newList = [ n + 1 for n in numbers ]
print(newList)

#   Ejemplo con Range
rangeList = [num * 2 for num in range(2,5)]
print(rangeList)

#   Ejemplo agregando condicionales
#   short_names = [new_item for item in list if test]
#   revisa en la lista los nombres con 4 letras o menos y los agrega en la nueva lista
names = ["Ricardo", "Alan", "Olaf", "Ian", "Daisy"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

#   Muestra los nombres con 5 o mas letras en mayusculas
long_names = [ name.upper() for name in names if len(name) >= 5 ]
print(long_names)