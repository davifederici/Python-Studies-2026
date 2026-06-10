"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Elabore um programa que leia um número e imprima todos os números de 1 até o número lido, e também o seu produto.
    Disciplina = Estrutura de repetição
    """

#Variável incial
a = int(input("Digite um valor:"))

#Fatorial
fat = 1

#Contador
cont = 1

#Estrutura de Repetição
while a >= cont:

    print(cont)

    fat = fat * cont

#Finalizar a repetição
    cont += 1

#exibir
print("Fatorial é:", fat)