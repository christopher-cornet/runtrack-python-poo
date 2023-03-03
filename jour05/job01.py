n = int(input('Renseignez un nombre:'))

def fact(n):
    if n < 2: # si le nombre est inférieur à 2, return 1
        return 1
    else:
        return n * fact(n-1) # sinon return nombre * nombre - 1
    
print(fact(n))