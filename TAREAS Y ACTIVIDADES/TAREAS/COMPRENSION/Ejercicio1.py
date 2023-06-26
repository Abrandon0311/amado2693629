#tamaño lista= 15 y 20
#datos dentro de la lista= 0 a 9

#buscar un numero ingresado por teclado en la lista
#decir si esta 
#decir si esta repetido
#decir si esta repetido, cuantas veces esta
#diga las posiciones donde lo encontro 

import random


lista=[random.randint(0,9) for i in range(random.randint(10,20))]
print(lista)
print(len(lista))

num_ingresado= int(input("ingrese un numero de 0 a 9:  "))
poscicion = 0
repeticion = 0
for i in lista:
    if i == num_ingresado:
        if i in lista:
            repeticion += 1
            poscicion = lista[i]   


if repeticion > 0:
    print(f"este numero se encuentra en la lista y se repite {repeticion} veces y se encuentra en la posicion ")
else:
    print("el numero no se encuentra")


