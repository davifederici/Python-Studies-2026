n = int(input("Digite um valor para n: "))

cont = 1
fatorial = 1
soma = 1

while cont <= n:

    fatorial = fatorial * cont

    soma = soma + (1 / fatorial)

    cont = cont + 1

print("O valor de S é:", soma)