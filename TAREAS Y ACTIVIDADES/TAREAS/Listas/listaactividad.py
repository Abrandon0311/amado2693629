import random
tam=random.randint(5,20)
lista=[random.randrange(100) for i in range(tam)]
rebanada=lista[3:7]
print(lista)
print(rebanada)

rebanada_mitad=lista[tam//2:]
print(rebanada_mitad)

