idade = int(input("Digite a sua idade:"))
cont = 0
while idade > 0 and idade <= 130:
    print("Idade válida:",idade)

    cont = cont + 1

    idade = int(input("Digite a sua idade:"))
print("Idades válidas:", cont)