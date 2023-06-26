from user import *
class stalf (user):
    def __init__(self, name, id, dept):
        user.__init__(self, name, id)
        self.__dept = dept
        
    def setdept(self, dept):
        self.__dept = dept
        
    def getdept(self,dept):
        return self.__dept