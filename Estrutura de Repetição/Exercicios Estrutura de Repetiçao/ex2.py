#Variável para indicar a quantidade de repetição
n_entrada = int(input("Digite o valor de entrada:"))

#Contador para encerrar a repetição
cont = 0

#Variável para fazer a conta e imprimir o que o eneunciado pede
triplo = 0

#Estrutura de repetição
while cont < n_entrada:

#Variável para imprimir os valores
    a = float(input("Digite um número:"))
    triplo = a * 3
    print("O valor de A é:", triplo)

#Fechamento da estrutura de repetição
    cont += 1