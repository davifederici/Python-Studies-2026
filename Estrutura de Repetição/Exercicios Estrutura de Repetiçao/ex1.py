#validar as variáveis A e B
a = int(input("Digite um valor:"))
b = int(input("Digite um valor:"))

#contador para fechar o while
cont = a

#estrutura de repetição para rodar o programa
while cont <= b:
    print(f"Os valoressão:", cont)

#Validando valores ímpares e multiplos de 3 na variável A
    if cont % 2 == 1:
        print("Os números ímpares de A são:", cont)
        if cont % 3 == 0:
            print("Os números ímpares e multiplos de 3 em A são:", cont)

#código para fechar a estrutura de repetição
    cont = cont + 1