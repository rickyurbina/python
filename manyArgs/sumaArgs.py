# El * indica un numero indefinido de argumentos
# en este ejercicio los argumentos son referenciados por su posicion 
def suma(*args):
    suma=0
    for n in args:
        suma = suma + n
    return suma
print(suma(1,2,3,4,5))


#   Ejemplo de kwargs.-  **kwargs:
#                        Many Keyworded Arguments

def calcula(**kwargs):
    print(kwargs)

calcula(suma=3, multiplica=5)

# Ejemplo de una clase con kwargs para inicializarla
class Auto:
    def __init__(self, **kw):
        self.marca = kw.get("marca")
        self.modelo = kw.get("modelo")
        self.color = kw.get("color")
        # se puede obtener el valor del argumento referenciadolo con el nombre
        self.asientos = kw["asientos"]
        # la diferencia es que con get, si el argumento no existe, lo inicializa con none y de la otra forma marca error si no existe algun valor

mi_auto = Auto(asientos=3)
print(mi_auto.marca)
