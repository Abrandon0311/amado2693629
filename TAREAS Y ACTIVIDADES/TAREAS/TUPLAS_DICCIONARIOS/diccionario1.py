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

