nb_list = [5, 10, 15, 80]
n = len(nb_list)

def returnLargest(nb_list, n):
    # si n == 1 return l'index 0 de la liste
    if n == 1:
        return nb_list[0]
    return max(nb_list[n - 1], returnLargest(nb_list, n - 1)) # return le plus grand nombre de la liste

print(returnLargest(nb_list, n))