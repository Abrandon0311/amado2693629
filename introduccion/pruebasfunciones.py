#suficiente para definir una funcion 
def prueba ():
    print("esto es una funcion")

prueba ()  #se llama la funcion y esto hace que imprima lo que esta en print  

#nueva funcion
def suma_valores (numero_uno, numero_dos): #se declaran dos variables que son numero uno y numero dos
    print(numero_uno + numero_dos) #se imprime en la consola las dos variables

suma_valores(5, 5)   #se ponen los numeros que se desean sumar 

def suma_valores_return (numero_uno, numero_dos): #se ponen las variables
    return numero_uno + numero_dos #se retorna

resultado = suma_valores_return(4, 4) #se declara una variable para suma y se llama a la funcion suma y se retorna
print(resultado) #se imprime la declaracion de la variable dando el resultado


def print_nombre(nombre, apellido):  #se declara la funcion y se ponen dos variables que son nombre y apellido 
    print(f"{nombre} {apellido}")  #se pone print para imprimir luego se pone la letra f para acceder a las variables que agregan cadenas de texto y por ultimo se agregan las variables
     
print_nombre("Brandon", "Amado")  #se llama la funcion y se reemplazan las variables con el nombre que nosotros deseemos

#funcion parametros por directo
def print_nombre_default(nombre, apellido, alias= "sin alias"): #se especifica exactamente dentro de un parametro lo que nosotros queremos que salga
    print(f"{nombre} {apellido} {alias}")
#si yo pongo el alias se me mostrara el resultado que yo ponga, pero si no pongo nada en alias el parametro especificara que no tengo un alias
print_nombre_default("Brandon", "Amado", "Amm" ) 
print_nombre_default("Brandon", "Amado",  )

#funcion que se encarga de imrpimir textos
def imprimir_texto(*texto): #se pone el asterisco para que se puedan poner mas de un parametro
    for texto in texto: #sepone el for texto in texto para que se impriman los parametros separados y sin los parentesis y comillas que hay en la linea de codigo
        print(texto)

imprimir_texto("hola mi nombre es", "Brandon Amado")    