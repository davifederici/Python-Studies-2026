""""
    Autor = Davi Federici Mendes Soares
    Exercicios = Uma empresa deseja aumentar seus preços em 20%. Faça um programa que leia o código e o preço de custo de produtos. Ao final da leitura, o programa deve exibir uma lista relacionando o código do produto ao seu novo preço, e finalmente o programa deve informar a média dos preços com e sem aumento. A entrada de dados deve terminar quando for lido um código de produto negativo.ura de repetição
    """

#Variável código
prod = int(input("Digite o código do produto:"))

#Contador
cont = 0
cont2 = 0

#Soma
soma = 0
soma2 = 0

preco1 = 0

while prod >= 0:

    preco = float(input("Digite o preço de custo do produto:"))

    preco1 = preco * 1.20

    print("--------------------")
    print("Código:", prod)
    print("O valor com aumento de 20 por cento foi de:R$ ", preco1)
    print("--------------------")

    soma += preco
    soma2 += preco1
    cont += 1
    prod = int(input("Digite o código do produto:"))

    if cont > 0:
        media = soma / cont
        media1 = soma2 / cont

        print("Média dos preços sem aumento:R$ ", media)
        print("Média dos preços com aumento:R$ ", media1)