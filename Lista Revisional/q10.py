x = int(input("Digite um valor:"))
soma = 0
soma2 = 0

for i in range(x):

    c = int(input("Digite o código:"))
    if c < 0:
        break

    p = float(input("Digite o preço:"))

    soma += p
    media1 = soma / x

    pn = p * 1.20

    soma2 += pn
    media2 = soma2 / x

    print("-------------------------------")
    print("Código:",c)
    print("Preço:",pn)
    print("-------------------------------")
print("\n")
print(f"Média antiga:{media1:.2f}")
print("Média nova:",media2)
print("-------------------------------")