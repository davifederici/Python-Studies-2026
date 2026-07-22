def soma(a,b):

    return a + b

def subtrair(a,b):

    return a - b

def multiplicar(a,b):

    return a * b

def dividir(a,b):

    if b == 0:
        return "Erro: divisão por zero"
    else:
        return a / b

def main():

    a = int(input("Digite um número:"))
    b = int(input("Digite um número:"))

    s = soma(a,b)
    su = subtrair(a,b)
    m = multiplicar(a,b)
    d = dividir(a,b)

    print("Soma:",s)
    print("Subtração:",su)
    print("Multiplicação:",m)
    print("Divisão:",d)

main()