"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Faça um programa que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. O final da leitura acontecerá quando for lido um valor negativo.
    Disciplina = Estrutura de repetição
    """

a = int(input("Digite um valor:"))

soma = 0
cont = 0

while a >= 0:
    
    soma += a
    cont +=1

    a = int(input("Digite um número:"))

if cont > 0:
    media = soma / cont
    print("A média é:", media)
else:
    print("Nenhum valor positivo informado")