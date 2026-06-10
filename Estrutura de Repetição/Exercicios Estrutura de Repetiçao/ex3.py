"""
    Autor = Davi Federici Mendes Soares
    Exercicios = Faça um programa que leia um valor indicando a quantidade de valores a ler em seguida. Um número deve ser lido por vez e seu programa deve classificá-lo como positivo ou negativo.
    Disciplina = Estrutura de repetição
    """

#Variável de valores a serem lidos
n_entrada = int(input("Digite os valores de entrada:"))

#Contador de repetição
cont = 0

#Estrutura de repetição para ler os números
while cont < n_entrada:
    
#Número informado pelo usuário
    a = float(input("Digite um número:"))

#Classificar o número informado como positivo ou negativo
    if a >= 0:
        print("Positivo")
    else:
        print("Negativo")
    
#Encerra a repetiçao
    cont += 1