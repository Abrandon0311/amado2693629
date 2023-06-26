import random

def generar_lista (n):
    lista= []
    for i in range(n):
        lista.append(random.randint(1,100))
    return lista

def imprimir_lista(lista):
    print(lista)    

def calcular_suma(lista):
    suma=sum(lista)
    print("la suma es", suma) 

def calcular_promedio(lista):
    promedio = sum(lista)/(len(lista))
    print("el promedio es", promedio)

def calcular_mayor(lista):
    num_mayor = min(lista)
    print("el numero mayor es", num_mayor)

def calcular_menor(lista):
    num_menor = min(lista)
    print("el numero menor es",num_menor)

def ordenar_ascendente(lista):
    lista_ordenada = sorted(lista)
    print("La lista ordenada de forma ascendente es", lista_ordenada)

def ordenar_descendente(lista):
    lista_ordenada = sorted(lista,reverse=True)
    print("La lista ordenada de forma descendente es", lista_ordenada)             


