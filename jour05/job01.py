n = int(input('Renseignez un nombre:'))

def fact(n):
    if n < 2: # si le nombre est inférieur à 2, return 1 et fin du programme
        return 1
    else:
        return n * fact(n-1) # sinon return nombre * nombre - 1 jusqu'à ce que nombre = 1
    
print(fact(n))

# La factorielle de n est: n * n - index:

# Pour 4:
# 4 * 3 = 12   # 4 * (4 - 1) = 12
# 12 * 2 = 24   # 12 * (3 - 1) = 24
# 24 * 1 = 24   # 24 * (2 - 1) = 24

# n * fact(n-1)