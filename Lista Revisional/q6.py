n = int(input("Digite um valor:"))

for i in range(n):

    x = int(input("Digite outro valor:"))

    if x > 0:
        print("Positivo")
    elif x < 0:
        print("Negativo")
    else:
        print("Zero")
