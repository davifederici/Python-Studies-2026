n = int(input("Digite um valor:"))
cont = 0
soma = 0

while n >= 0:
    soma = soma + n
    cont = cont + 1

    n = int(input("Digite um número:"))

    media = soma / cont

print("O valor da média é:", media)