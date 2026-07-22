def inverso(n,invertido = 0):

    if n == 0:
        return invertido

    return inverso(n // 10, invertido * 10 + (n % 10))


def main():

    n = int (input("Digite um valor:"))

    resultc = inverso(n)

    print("O inverso é:", resultc)

main()