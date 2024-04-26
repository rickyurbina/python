#   tomar una lista del usuario, convertirla en numeros enteros
#   separar los numeros pares y nones

lista_de_strings = input().split(',')

#   creamos lista de numeros cambiandolos a entero
numeros = [int(x) for x in lista_de_strings]

#   Creamos la lista de pares comparando si el numero es divisible entre 2 con el modulo %

pares = [num for num in numeros if num%2 == 0]

print(pares)