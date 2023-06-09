


class user:
    def __init__(self,name,code):
        self.__name = name
        self.__code = code
        self.__books=[]
    
    def setname(self,name):
        self.__name = name
    
    def getname(self):
        return self.__name
    
    def setcode(self,code):
        self.__code = code
    
    def getcode(self):
        return self.__code

    def agegarbooks (self,books,account):
        self.__books.append(account)
        
    def accountbook(self, account):
        borrowed= input ('Nombre del libro:  ')
        reversed= input ('Dia de la reservacion:   ')
        returned= input ('Dia de la entrega:  ')
        lost= input ('¿Libro perdido (SI/NO)?:  ')
        objaccount=account(borrowed, reversed, returned, lost)
        self.__account.append(objaccount)
    def veraccount (self):
        return self.__account
