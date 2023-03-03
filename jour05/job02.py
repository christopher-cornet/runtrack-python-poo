def power(x, n):
    if n == 0: # Si l'exposant n = 0 return 1
        return 1
    else:
        return (x * power(x, n-1)) # sinon x * x et n-1
    
print(power(4, 5))