#diccionario de colores de español a ingles, minimo 10 colores
diccionario = {"rojo": "red",
               "azul": "blue",
               "blanco": "white",
               "negro": "black",
               "amarillo": "yellow",
               "rosado": "pink",
               "naranja": "orange",
               "morado": "purple",
               "cafe": "brown",
               "verde": "green"}

colores = ['rojo', 'azul', 'blanco', 'negro', 'amarillo', 'rosado', 'naranja', 'morado', 'cafe', 'verde']

for color in colores:
    if color in diccionario:
        print(color, "->", diccionario[color])
    else: 
        print(color, "no esta en el diccionario")
#PREGUNTAS
#que es una lista multidimensional 
#que es un parametro de una funcion y que papel desempeña
#que hace la instruccion return 

#CODIGO
#ay partes del codigo las cuales no son funciones y ay otras que no tienen nada que ver con lista
#con respecto a los diccionarios no hay funciones declaradas por la cual no se considera un modulo utilizable