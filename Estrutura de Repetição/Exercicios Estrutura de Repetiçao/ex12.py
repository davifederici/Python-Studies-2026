""""
    Autor = Davi Federici Mendes Soares
    Exercicios = A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e número de filhos. A prefeitura deseja saber:
a. Média do salário da população.
b. Média do número de filhos.
c. Maior salário.
d. Percentual de pessoas com salário até R$100,00.
O final da leitura de dados se dará com a entrada de um salário negativo.
    Disciplina = Estrutura de repetição
    """

#Variável para salário
n = float(input("Digite seu sálario:"))

#Contador
cont = 0

#Soma
soma = 0
soma2 = 0

#Maior Salário
maior = 0

#Percentual
ate100 = 0

#Estrutura de repetição
while n > 0:
#Variável para filhos
    f = int(input("Digite o número de filhos:"))

    soma += n
    soma += f
    cont += 1

    if n > maior:
        maior = n

    if n <= 100:
        ate100 += 1

    n = float(input("Digite seu salário:"))

    if cont > 0:
        media = soma / cont
        mediaf = soma2 / cont
        percentual = (ate100/cont) * 100

        print("Média salárial:", media)
        print("Média de filhos:", mediaf)
        print("O maior salário é:", maior)
        print("O percentual foi de:", percentual,"%")
    else:
        print("Nenhum dado informado")