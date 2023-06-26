class book :
    def __init__(self, title, author, code, publication):
        self.__title = title
        self.__author = author
        self.__code = code
        self.__publication = publication
        
    def settitle(self, title):
        self.__title = title
        
    def gettitle(self):
        return self.__title
    
    def setauthor(self, author):
        self.__author = author
        
    def getauthor(self):
        return self.__author
    
    def setcode(self, code):
        self.__code = code
        
    def geetcode(self):
        return self.__code
    
    def setpublication(self, publication):
        self.__publication = publication
        
    def getpublication(self):
        return self.__publication        
