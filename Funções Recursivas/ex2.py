def multi(a,b):
    if b == 1:
        return b
    else:
        return a + multi(a, b - 1)

print(multi(5,5))