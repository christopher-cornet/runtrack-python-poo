class Livre:
    def __init__(self, title, author, nbpages):
        self.__title = title
        self.__author = author
        self.__nbpages = nbpages

    def getbook(self):
        return self.__title, self.__author, self.__nbpages
    
    def setbook(self, title2, author2, nbpages2):
        self.__title = title2
        self.__author = author2
        if nbpages2 > 0:
            if type(nbpages2) is int:
                self.__nbpages = nbpages2
        return self.__title, self.__author, self.__nbpages
    
newBook = Livre('Germinal', 'Émile Zola', 250)

print('Get:', newBook.getbook())

print('Set:', newBook.setbook('Steve Jobs', 'Walter Isaacson', 420))