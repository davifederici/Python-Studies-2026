def factorial(n):
    
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():

    n = int(input("Digite um valor:"))

    prod = factorial(n)

    print("Produto:", prod)

main()