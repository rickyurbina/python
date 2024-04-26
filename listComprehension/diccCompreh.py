#   forma general para usar list Comprehension en diccionarios
#   desde una lista:
#   new_dict = {new_key:new_value for item in list}

#   desde un diccionario existente
#   new_dict = {new_key:new_value for key:value in dict.items()}


#   desde un diccionario existente agregando condicionales
#   new_dict = {new_key:new_value for key:value in dict.items() if test }


#   reto 1:  de una lista de nombres, asignarles una calificacion aleatoria y agregar nombre y calificacion a un diccionario
#   despues, crear un diccionario con los alumnos aprovados
import random
names = ["Ricardo", "Alan", "Olaf", "Ian", "Daisy"]

calificaciones = { alumno:random.randint(1,100) for alumno in names }
print(calificaciones)

aprovados = {alumno:calif for (alumno,calif) in calificaciones.items() if calif > 59 }
print(aprovados)