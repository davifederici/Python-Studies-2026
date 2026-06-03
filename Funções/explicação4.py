def divisao(x):
    a = x + x
    return a

b = int(input("Digite um número: "))
cont = 1
soma = 0

while b >= cont:
    if b % cont == 0:
        soma = soma + cont

    cont = cont + 1

print("A soma será:", soma)
print(divisao(b))