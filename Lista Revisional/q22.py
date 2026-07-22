def soma_par(n):

    soma1 = 0

    for i in n:

        if i % 2 == 0:
            soma1 += i
        
    return soma1
    
def media_num(n):

    soma = 0
    cont = 0

    for num in n:
        soma += num

    media = soma / len(n)

    return media
    
def main():

    guarda = []
    resultado_media = 0
    soma_num = 0
    maior = 0
    qnt = 0

    a = int(input("Digite a quantidade de vezes:"))

    for i in range(a):

        n = int(input(f"Digite o {i + 1} número:"))

        while n < 0:

            n = int(input("Inválido. Digite novamente:"))

        guarda.append(n)

    resultado_media = media_num(guarda)
    soma_num = soma_par(guarda)

    print("-------------------------------")
    print("A soma de todos os números pares é:", soma_num)

    print("A média é:",resultado_media)

    for g in guarda:

        if g > resultado_media:
            qnt +=1

    print("Os números maiores que a média são:",qnt)

main()