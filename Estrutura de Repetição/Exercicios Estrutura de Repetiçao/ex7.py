cont = 0

valor = int(input("Digite um valor: "))

maior = valor
menor = valor

cont = 1

while cont < 50:

    valor = int(input("Digite um valor: "))

    if valor > maior:
        maior = valor

    if valor < menor:
        menor = valor

    cont = cont + 1

print("O maior valor é:", maior)
print("O menor valor é:", menor)