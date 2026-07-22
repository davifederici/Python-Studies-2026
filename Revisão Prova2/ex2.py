def calcular_consumo(d):

    soma = 0

    for i in range(d):
        c = int(input(f"Digite o consumo do dia {i + 1} (litros):"))

        soma += c
    print("\n")
    print(f"Consumo total: {soma} litros")
    print("\n")

def main():
    while True:

        x = int(input("Digite a quantidade de residências:"))

        cont = 0

        while x > cont:

            m = input("Digite seu nome:")
            d = int(input("Digite os dias monitorados:"))
            print("\n")

            if d > 0:
                calcular_consumo(d)

            cont += 1
        resposta = input("Deseja cadastrar outra residência? (S/N):")

        if resposta.lower() != "s":
            print("Programa Encerrado")
            break

main()