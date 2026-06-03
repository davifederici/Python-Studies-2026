n = int(input("Digite um número:"))
cont = 0
soma = 0

while n != 0:

    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1 

    n = int(input("Digite um valor:"))

media = soma / cont
print("O valor é:", media)