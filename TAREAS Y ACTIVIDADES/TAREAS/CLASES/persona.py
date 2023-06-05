class Persona:
    def __init__(self,nombre,documento):
        self.__nombre=nombre
        self.__documento=documento
        self.__curso=[]
        
    def setNombre(self, nombre):
        self.__nombre=nombre

    def getNombre(self):
        return self.__nombre
    
    def setdocumento(self, documento):
      self.__documento=documento

    def getdocumento(self):
      return self.__documento      
    
    
    def setCurso(self, curso):
        self.__curso.append(curso)

    def getCurso(self):
        return self.__curso
    
    def deleteCurso(self, curso):
        if curso in self.__curso:
            self.__curso.remove(curso)
        else:
            print("Este curso no se encuentra en la lista")        

       


