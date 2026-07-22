def soma_digitos(numero):
    if numero == 0:
        return 0
    else:
        # n % 10 pega o ultimo digito
        # n //10 remove o ultimo digito
        return (numero % 10) + soma_digitos(numero // 10)
    
def main():

    numero = int(input("Digite um número:"))

    resultado = soma_digitos(numero)

    print("Soma dos digitos:",resultado)

main()