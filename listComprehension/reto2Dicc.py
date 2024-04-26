# A partir de un diccionario con dias y temperaturas en grados C de la semana
# generar un diccionario con los dias y temperaturas en grads F

clima_c = eval(input())

clima_f = {dia:temp * 9/5 +32 for (dia, temp) in clima_c.items() }

print(clima_f)
