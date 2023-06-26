from library import *

class book (library):
    def __init__(self, Titulo:str, Autor:str, ISBN:str, Publicacion:str):
        self.__autor = Autor 
        self.__titulo = Titulo
        self.__isbn = ISBN
        self.__publicacion = Publicacion
        self.__estado = None


    