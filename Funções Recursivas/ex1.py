def positivo(n):
    if n == 0:
        return 0
    else:
        return n  + positivo(n - 1)
    
print(positivo(10))