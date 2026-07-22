def soma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + soma_digitos(n // 10)
    
def main():

    n = int(input("Digite um número:"))

    result = soma_digitos(n)

    print("A soma dos dígitos é:",result)

main()