n = int(input("Digite um número:"))

soma = 0
qnt = 0

for i in range(n):

    a = int(input("Digite um valor:"))

    if a % 2 == 0:
        soma += a
        qnt += 1

if qnt > 0:
    media = soma / qnt

print("A média dos pares é:", media)
    