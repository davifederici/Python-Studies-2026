def main():
    n = int(input("Digite um número:"))
    result = 0

    for i in range(n - 1):
        n = int(input("Digite um valor:"))

        result = n * 3

        print("O número é:",n)
        print(f"O triplo de {n} é:", result)

main()