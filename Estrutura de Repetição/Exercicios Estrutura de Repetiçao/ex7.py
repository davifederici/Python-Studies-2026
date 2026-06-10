"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Escreva um programa que leia 50 valores e encontre o maior e o menor deles. Mostre o resultado.
    Disciplina = Estrutura de repetição
    """

#Definir a variável para os 50 valores
a = 50

#Variável de valor incial
b = int(input("Digite um valor:"))
#Contador
cont = 1

#Menor valor
menor = b

#Maior valor 
maior = b

#Estrutura de Repetição
while a > cont:
    if b > maior:
        maior = b
    
    elif b < menor:    
        menor = b
    
    b = int(input("Digite um valor:"))

#Finalizar a repetição
    cont += 1

#Exibir valores
print("O maior valor é:", maior)
print("O menor valor é:", menor)