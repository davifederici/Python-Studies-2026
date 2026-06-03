n = int(input("Digite um número:"))
cont = 0
neg = 0
while n > cont:

    valor = int(input("Digite um valor:"))

    if valor < 0:
        neg = neg + 1

    cont = cont + 1

print("Quantidade de valores negativos:", neg)