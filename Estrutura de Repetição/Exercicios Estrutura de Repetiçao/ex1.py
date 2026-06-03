a = int(input("Digite um número: "))
b = int(input("Digite um número: "))

while a <= b:

    print("Valor de A:", a)
    print("Valor de B:", b)

    if a % 2 == 1:
        print("A é ímpar:", a)

    if a % 3 == 0:
        print("A é múltiplo de 3:", a)

    if b % 2 == 1:
        print("B é ímpar:", b)

    if b % 3 == 0:
        print("B é múltiplo de 3:", b)

    a = int(input("Digite um número: "))
    b = int(input("Digite um número: "))