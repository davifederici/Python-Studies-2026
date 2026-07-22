def soma_digitos(numero):

    if numero == 0:
        return 0
    else:
        return (numero % 10) + soma_digitos(numero // 10)
    
def main():

    numero = int(input("Digite um número:"))

    r = soma_digitos(numero)

    print("Soma dos dígitos:",r)

main()