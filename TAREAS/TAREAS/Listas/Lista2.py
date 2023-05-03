#hacer un programa que de la suma de los numeros, el promedio y numero mayor y menor de numeros aleatorios 
import random
lista=[]
tamaño=int(random.randint(10,20))
print(tamaño)
suma=0
num_mayor=0
num_menor=999
mediana=0
for i in range(tamaño):
    num=(random.round()*100)
    lista.append(num)
    suma += num
    promedio= suma / tamaño
    if num > num_mayor:
        num_mayor= num
    if num < num_menor:
        num_menor= num    
    if num >0.0:
        mediana=(num_mayor + num_menor) / 2  

    
print(lista)
print(f"la suma de los numeros en la lista es {suma}")
print(f"el pormedio de la suma de los numeros es {promedio}")
print(f"el numero mayor generado en la lista es {num_mayor}")
print(f"el numero menor generado en la lista es {num_menor}")
print(f"la mediana de los numeros es {mediana}")