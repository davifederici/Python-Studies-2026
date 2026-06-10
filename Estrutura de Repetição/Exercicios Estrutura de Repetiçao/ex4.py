"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Escreva um programa que leia valores, um de cada vez, e conte quantos destes valores são negativos, escrevendo esta informação na tela.
    Disciplina = Estrutura de repetição
    """

#Variável de entrada
n_entrada = int(input("Digite um valor de entrada:"))

#Contador de repetição
cont = 0

#Valores negativos
neg = 0

#Estrutura de repetição
while cont < n_entrada:

#Valores escritos pelo usuário
    a = float(input("Digite um valor:"))

#Condição para achar os valores negativos
    if a < 0:
        neg += 1

#Finalizar a repetição
    cont += 1
    
#Exibir resultado
print("Quantidade de números negativos:", neg)