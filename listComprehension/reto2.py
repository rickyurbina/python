#   Compara el contenido de dos arhivos y muestra una lista de los elementos que existen en los dos archivos
#   Los archivos tienen una lista de numeros diferentes
#   el resultado debe ser una lista de numeros

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

#   con list comprehension recorremos las dos listas y vamos comparando sus valores
#   cambiamos los valores an int para cumplir con el requisito del reto
result = [int(num) for num in list1 if num in list2]

print(result)