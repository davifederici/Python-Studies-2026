n = int(input("Digite um número:"))

fatorial = 1
cont = 1

while cont <= n:
    fatorial = fatorial * cont
    cont = cont + 1

print("O valor de n é:",fatorial)