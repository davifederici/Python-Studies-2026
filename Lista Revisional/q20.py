def factorial(f):
    
    if f == 1:
        return 1
    else:
        return f * factorial( f - 1)
    
def main():

    f = int(input("Digite um número:"))

    resultado = factorial(f)

    print("Produto:",resultado)

main()