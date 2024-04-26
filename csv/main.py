# import csv

# with open("pandas --versionweather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1]!= "temp":
#             temps.append(int(row[1]))

#     print(temps)

import pandas
data = pandas.read_csv("weather_data.csv")

#convertir los datos a diccionario
data_dict = data.to_dict()
print(data_dict)

#convierte los datos a una lista
data_list = data["temp"].to_list()
print(len(data_list))

#Obtener el maximo y el promedio de la lista
print(data.temp.max())
print(data.temp.mean())

#obtener los datos por columna
print(data["temp"])
print(data.temp)

# Obtener los datos por renglon
print(data[data.day == "Monday"])

# Cual es el dia con la teperatura maxima ?
print("Temperatura maxima")
print(data[data.temp == data.temp.max()])

# Obtener una temperatura maxima y convertirla a farenheith
maxima = data[data.temp == data.temp.max()]
max_F = (maxima.temp * (9/5)) + 32
print(max_F)

# Crear un dataFrame con datos generados en python y exportarlos a un archivo CSV
data_dicc = {
    "students": ["Rick", "Monica", "Mel"],
    "scores": [5,7,2]
}
datos = pandas.DataFrame(data_dicc)
datos.to_csv("new_data.csv")