class Livre:
    def __init__(self, title, author, nbpages):
        self.__title = title
        self.__author = author
        self.__nbpages = nbpages
        self.__disponible = True

    def getbook(self):
        return self.__title, self.__author, self.__nbpages
    
    def setbook(self):
        if self.__nbpages < 0:
            print('Erreur, le nombre doit être un nombre entier positif.')
            return self.__title, self.__author, self.__nbpages
        elif type(self.__nbpages) is not int:
                print('Erreur, le nombre doit être un nombre entier positif.')
                return self.__title, self.__author, self.__nbpages
        else:
            self.__nbpages = 500
            return self.__title, self.__author, self.__nbpages
        
    def vérification(self):
        # Vérif si livre est disponible
        if self.__disponible == True:
            return True
        else:
            return False
        
    def emprunter(self):
        # Si la vérif est true et donc si le livre est disponible
        # alors emprunter = True et disponible devient False sinon emprunter = False
        if self.vérification() == True:
            self.__disponible = False
            return True
        else:
            return False
        
    def rendre(self):
        # Si l'emprunt = True, disponible devient True sinon
        if self.emprunter() == True:
            if self.vérification() == False:
                self.__disponible = True
                return True
        else:
            return False

newBook = Livre('Les misérables', 'Victor Hugo', 250)

print('Get:', newBook.getbook())

print('Set:', newBook.setbook())

print('Verification:', newBook.vérification())

print('Emprunter:', newBook.emprunter())

print('Rendre:', newBook.rendre())