"""
Autor = Davi Federici Mendes Soares
Exercício = Faça um programa que imprima a média de números excluindo o menor e o maior deles.
Disciplina = Estrutura de repetição
"""

n = int(input("Quantos números serão digitados? "))

if n <= 2:
    print("Erro! É necessário informar mais de 2 números.")
else:

    valor = float(input("Digite um número: "))

    maior = valor
    menor = valor
    soma = valor

    cont = 1

    while cont < n:

        valor = float(input("Digite um número: "))

        soma += valor

        if valor > maior:
            maior = valor

        if valor < menor:
            menor = valor

        cont += 1

    media = (soma - maior - menor) / (n - 2)

    print("Maior valor:", maior)
    print("Menor valor:", menor)
    print("Média sem o maior e o menor:", media)