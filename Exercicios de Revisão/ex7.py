h = int(input("Digite a quantidade de horas:"))
if h > 0:
    if h <= 2:
        valor = h * 8
        print(f"O valor a ser pago é: R$ {valor}")
    elif h > 2 and h <= 5:
        valor = h * 6.50
        print(f"O valor a ser pago é: R$ {valor}")
    elif h > 5:
        valor = h * 5
        print(f"O valor a ser pago é: R$ {valor}")
    else:
        print("Valor inválido")
else:
    print("Valor inválido")