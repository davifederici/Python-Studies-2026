n = int(input("Digite a quantidade de números: "))

if n <= 2:
    print("Erro! É necessário digitar mais de 2 números.")

else:

    cont = 0
    soma = 0

    valor = int(input("Digite um valor: "))

    maior = valor
    menor = valor

    while cont < n:

        if cont > 0:
            valor = int(input("Digite um valor: "))

        soma = soma + valor

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        cont = cont + 1

    media = (soma - maior - menor) / (n - 2)

    print("A média excluindo o maior e o menor é:", media)