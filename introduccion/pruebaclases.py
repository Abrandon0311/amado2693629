class Persona:  #se define la clase
    pass 

print(Persona( ))

class Person: #se tiene la capacidad para que la clase persona reciba algun parametro 
    def __init__(self, nombre, apellido): #init se crea para hacer un constructor de clases
        self.nombre = nombre
        self.apellido = apellido

mi_persona = Person("Brandon", "Amado")
print(f"{mi_persona.nombre} {mi_persona.apellido}")