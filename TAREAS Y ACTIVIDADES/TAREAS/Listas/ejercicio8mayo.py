#llenar una lista con un numero aleatorio (reales con un decima) que representen calificaciones de un curso.
#Se evalua de 0 a 5.
#el curso puede tener entre 20 y 30 aprendices.
#Hallar 
#1.Genere listas nuevas para los aprobados y reprobados (se aprueba con 3)
#2.Genere listas nuevas por cada unidad decimal. Es decir, los que sacan 0 a 1 son un grupo, los de  1 a 2 otros grupo y asi sucesivamente.
#3.Diga cual es el promedio de los que aprueban y de los que reprueban por separado.

import random


calificaciones = [] # Creamos una lista vacía para almacenar las calificaciones

# Generamos calificaciones aleatorias para un curso de entre 20 y 30 aprendices
num_aprendices = random.randint(20, 30)
for i in range(num_aprendices):
    calificacion = round(random.uniform(0, 5), 1)
    calificaciones.append(calificacion)

# Separamos las calificaciones de aprobados y reprobados
aprobados = []
reprobados = []
for calificacion in calificaciones:
    if calificacion >= 3:
        aprobados.append(calificacion)
    else:
        reprobados.append(calificacion)

# Separamos las calificaciones por unidad decimal
grupos = {}
for calificacion in calificaciones:
    unidad_decimal = int(calificacion)
    if unidad_decimal not in grupos:
        grupos[unidad_decimal] = []
    grupos[unidad_decimal].append(calificacion)

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
