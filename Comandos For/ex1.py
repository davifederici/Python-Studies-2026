def main():
    a = int(input("Digite um número:"))
    b = int(input("Digite um número:"))

    if b < a:
        print("Programa encerrado")

    for i in range(a, b + 1):
        if i % 2 == 1:
            print("Números ímpares:",i)
        
        if i % 3 == 0:
            print("Os números divisiveis por 3 são:",i)

main()