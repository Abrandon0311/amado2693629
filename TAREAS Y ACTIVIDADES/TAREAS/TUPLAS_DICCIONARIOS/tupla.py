#llene una tupla con numeros aleatorios entre 0 y 100 y el tamaño de la tupla sea aleatorio de maximo 20 y imprimirla 
import random

tamaño = random.randint(1, 20)  # Genera un tamaño aleatorio entre 1 y 20
tupla = tuple(random.randint(0, 100) for _ in range(tamaño))  # Genera los números aleatorios y crea la tupla

print(tupla)  # Imprime la tupla generada
