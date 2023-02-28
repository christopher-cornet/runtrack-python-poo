class Student:
    def __init__(self, prenom, nom, idstudent, nbcredits):
        # Créer une classe nommée “Student” qui a comme attributs privés un nom, un prénom
        # un numéro d’étudiants et un nombre de crédits par défaut à zéro.
        self.__prenom = prenom
        self.__nom = nom
        self.__idstudent = idstudent
        self.__nbcredits = nbcredits
        # Ajouter l’attribut privé nommé “level” dans le constructeur de la classe “Student”
        # qui prend en valeur la méthode “studentEval”.
        self.__level = self.__studentEval()
        
    # “add_credits” permet d’ajouter un nombre de crédits au total de celui de l’étudiant.
    # Ce mutateur doit s’assurer que la valeur passée en argument est supérieure à zéro pour
    # garantir l’intégrité de la valeur.
    def add_credits(self, nbcredits):
        # Ajouter des credits à trois reprises et imprimer son total de crédits en console.
        self.__nbcredits += nbcredits
        self.__nbcredits += nbcredits
        self.__nbcredits += nbcredits
        self.__level = self.__studentEval()

        print('Le nombre de credits de', self.__prenom, self.__nom, 'est de', self.__nbcredits, 'points')

    def __studentEval(self):
        if self.__nbcredits >= 90:
            return 'Excellent'
        elif self.__nbcredits >= 80:
            return 'Très bien'
        elif self.__nbcredits >= 70:
            return 'Bien'
        elif self.__nbcredits >= 60:
            return 'Passable'
        elif self.__nbcredits < 60:
            return 'Insuffisant'
        
    # Créer une méthode studentInfo qui écrit en
    # console les informations de l’étudiant (nom, prénom, identifiant et son niveau).
    def studentInfo(self):
        print('Prenom =', self.__prenom)
        print('Nom =', self.__nom)
        print('Id =', self.__idstudent)
        print('Level =', self.__level)

student = Student('John', 'Doe', 145, 60)

student.add_credits(10)

student.studentInfo()