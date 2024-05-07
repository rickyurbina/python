def suma(*args):
    sum=0
    for n in args:
        sum += n
    return sum

print(suma(2,3,4,5))

def materias(**kwargs):
    for key, value in kwargs.items():
        print(kwargs)

materias(mate=9, quiumica=8,Progra =9)