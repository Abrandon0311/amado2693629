from user import *
class account (user):
    def __init__(self, name, code, borrowed_book, reserved_book,returned_book, lost_book, fine_amount ):
        user.__init__(name,code)
        self.__borrowed_book = borrowed_book
        self.__reserved_book = reserved_book
        self.__returned_book = returned_book
        self.__lost_book = lost_book
        self.__fine_amount = fine_amount
    
    def setborrowed_book(self, borrowed_book):
        self.__borrowed_book = borrowed_book
    
    def getborrowed_book(self):
        return self.__borrowed_book
    
    def setreserved_book(self, reserved_book):
        self.__reserved_book = reserved_book
        
    def getreserved_book(self):
        return self.__reserved_book
    
    def setreturned_book(self, returned_book):
        self.__returned_book = returned_book
        
    def getreturned_book(self):
        return self.__returned_book
    
    def setlost_book(self, lost_book):
        self.__lost = lost_book
    
    def getlost_book (self, lost_book):
        return self.__lost_book
    
    def setfine_amount (self, fine_amount):
        self.__fine_amount = fine_amount
        
    def getfine_amount (self):
        return self.__fine_amount
    
    