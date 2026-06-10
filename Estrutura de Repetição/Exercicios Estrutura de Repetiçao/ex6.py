"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Escreva um programa que calcule a média dos números digitados pelo usuário se eles forem pares. Termine a leitura se o usuário digitar 0.
    Disciplina = Estrutura de repetição
    """

#Variável inicial que será usada na repetiçao
a = float(input("Digite um valor:"))

#Contador
cont = 0

#Soma
soma = 0

#Estrutura de repetição
while a != 0:

    if a % 2 == 0:
        soma += a
        cont += 1

    a = float(input("Digite um valor:"))

#Calculo da média de valores pares
if a % 2 == 0:
    media = soma / cont
    print("Os valores pares serão:",media)