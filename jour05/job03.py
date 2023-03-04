def returnLength(string1):
    if string1 == '': # Si la chaine de caractère ne contient pas de caractère return 0
        return 0
    else:
        return 1 + returnLength(string1[1:]) # Sinon Return 1 et longueur de la string -1

print(returnLength('Echecs'))
