"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Escreva um algoritmo que lê um valor n inteiro e positivo, e calcula e escreve o valor de S para a equação abaixo:
    """
#Variável n
n = int(input("Digite um valor:"))

#Fatorial
fat = 1

#Contador
cont = 1

#Soma da série
S = 1

#Estrutura de Repetição
while n >= cont:

    fat *= cont

    S += 1/fat

#Finalizar a estrutura
    cont += 1

#Exibir valor
print("O resultado da equação é:", S)