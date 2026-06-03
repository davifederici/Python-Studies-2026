n = int(input("Digite um número:"))

fatorial = 1
cont = 1

while n >= cont:
    fatorial *= cont
    cont = cont + 1
    print("O valor é:", fatorial)