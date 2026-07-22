def calcular_consumo(d):

    soma = 0

    for i in range(d):
        c = float(input(f"Digite o consumo do {i + 1} dia:"))

        while c <= 0:
           print("Consumo inválido")
           c = float(input("Digite novamente:"))

        soma += c

    return soma


def main():

    while True:

        r = int(input("Digite a quantidade de residências:"))

        for i in range(r):

            d = int(input(f"Digite a quantidade de dias {i + 1} residência:"))

            while d <= 0:
                print("Dias inválidos:")
                d = int(input("Digite a quantidade de dias:"))
            
            consumo = calcular_consumo(d)

            print(f"O conusmo total foi de:{consumo} litros")

        x = (input("Deseja finalizar?"))

        if x.lower() != "s":
            print("Programa encerrado")
            break

main()