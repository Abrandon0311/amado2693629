import random

# Generamos calificaciones aleatorias para un curso de entre 20 y 30 aprendices
num_aprendices = random.randint(20, 30)
calificaciones = [round(random.uniform(0, 5), 1) for i in range(num_aprendices)]

# Separamos las calificaciones de aprobados y reprobados utilizando slicing
aprobados = calificaciones[calificaciones.index(3.0):]
reprobados = calificaciones[:calificaciones.index(3.0)]

# Separamos las calificaciones por unidad decimal utilizando slicing
grupos = {}
for i in range(6):
    grupo = [calificacion for calificacion in calificaciones if int(calificacion) == i]
    grupos[i] = grupo

# Calculamos los promedios de aprobados y reprobados
promedio_aprobados = sum(aprobados) / len(aprobados)
promedio_reprobados = sum(reprobados) / len(reprobados)

# Imprimimos los resultados
print("Calificaciones del curso:", calificaciones)
print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
for unidad_decimal, grupo in grupos.items():
    print("Calificaciones entre", unidad_decimal, "y", unidad_decimal + 1, ":", grupo)
print("Promedio de aprobados:", promedio_aprobados)
print("Promedio de reprobados:", promedio_reprobados)
