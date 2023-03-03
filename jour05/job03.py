def returnLength(string1):
    if string1 == '': # Si la chaine de caractère ne contient pas de caractère
        return 0
    else:
        return 1 + returnLength(string1[1:]) # Return longueur de la string

print(returnLength('Echecs'))