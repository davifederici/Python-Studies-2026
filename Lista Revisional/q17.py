def calcular_consumo(dias):

    soma = 0

    for i in range(dias):
    
        c = float(input("Digite o consumo de água em litros:"))

        while c < 0:
            c = float(input("Digite um número válido:"))

        soma += c

    return soma

def main():

    while True:

        r = int(input("Digite a quantidade de residências:"))

        n = input("Digite seu nome:")

        dias = int(input("Digite quantos dias foi monitorido:"))

        while dias < 0:
            
            dias = int(input("Dias inválidos. Digite novamente:"))

        consumo = calcular_consumo(dias)

        print(f"Consumo total: {consumo} litros")

        cadastro = input("Deseja cadastrar outra residência? (S/N):")

        if cadastro != "s":
            break

main()