def main():

    n = 10
    soma = 0

    for i in range(n):

        x = int(input("Digite um valor:"))

        while x <= 0:
            x = int(input("Digite novamente:"))

        soma += x

    media = soma / n

    print("A média de é de:",media)

main()