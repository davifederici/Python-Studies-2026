n = int(input("Digite um número:")) 
j = int(input("Digite um número:")) 
i = int(input("Digite um número:")) 

cont = 0
numero = 0

while n > cont:
    if numero % i == 0 or numero % j == 0:
        print(numero)

        cont = cont + 1
    numero = numero + 1