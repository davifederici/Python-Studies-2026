def soma(n):

    somar = 0

    for i in range(0, n + 1):

        if i % 3 == 0:
            somar += i

    return somar
    
def main():
    
    n = int(input("Digite um valor:"))

    while n < 3:
        n = int(input("Número inválido. Digite um número maior que 3:"))

    resultado = soma(n)

    print("A soma é:",resultado)

main()