x = int(input("Digite a quantidade de alunos:"))

soma = 0
qnt = 0
nota = []

for i in range(x):

    a = float(input("Digite um nota:"))

    while a < 0 or a > 10:
        print("Valor inválido")
        a = float(input("Digite um nota:"))

    soma += a
    nota.append(a)

media = soma / x

for nota in nota:
    if nota >= media:
        qnt += 1

print("A média é:", media)
print("Maior que a média:",qnt)