#crea un diccionario a partir de una frase, cada elemento del diccionario debe ser una palabra y el numero de letras que tiene esa palabra

frase = input()

res = { palabra:len(palabra) for palabra in frase.split() }

print(res)