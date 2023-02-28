class Livre:
    def __init__(self):
        self.__title = 'Harry Potter'
        self.__author = 'J. K. Rowling'
        self.__nbpages = 11.5

    def getbook(self):
        return self.__title, self.__author, self.__nbpages
    
    def setbook(self):
        if self.__nbpages < 0 or type(self.__nbpages != int):
            print('Erreur, le nombre doit être un nombre entier positif.')
            return self.__title, self.__author, self.__nbpages
        else:
            self.__nbpages = 500
            return self.__title, self.__author, self.__nbpages
    
newBook = Livre()

print('Get:', newBook.getbook())

print('Set:', newBook.setbook())