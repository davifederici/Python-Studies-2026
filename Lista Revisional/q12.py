def inverso(n,invertido = 0):
    if n == 0:
        return invertido
    else:
        return inverso(n // 10, invertido * 10 +(n % 10))
def main():

    n = int(input("Digite um valor:"))

    result = inverso(n)

    print("O inverso é:",result)

main()