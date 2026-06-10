"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Escreva um programa que dado um número inteiro calcule (fatorial).
    Disciplina = Estrutura de repetição
    """

#Variável incial
n = int(input("Digite o valor:"))

#Fatorial
fat = 1

#Contador
cont = 1

#Estrutura de Repetição
while n >= cont:

#Exibir n!
    print(f"{cont}!")

#Cálculo fatorial
    fat *= cont

#Finalizar a repetição
    cont += 1

#Exibir resultado
print("Resultado:", fat)
