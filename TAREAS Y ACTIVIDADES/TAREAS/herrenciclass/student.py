from user import *
class student (user):
    def __init__(self, name, id, course):
        user.__init__(self, name, id, course)
        self.course = course
        
    def setcourse(self, course):
        self.__couser = course
    
    def getcourse(self, course):
        return self.__course
        