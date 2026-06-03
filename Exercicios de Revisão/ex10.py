consumo = float(input("Digite o consumo de energia:"))
if consumo >= 0:
    if consumo <= 100:
        valor = consumo * 0.60
        print(f"O valor é: R$ {valor:.2f}")
    elif consumo > 100 and consumo <= 300:
        valor = consumo * 0.50
        print(f"O valor é: R$ {valor:.2f}")
    else:
        valor = consumo * 0.40
        print(f"O valor é de: R$ {valor}")
else:
    print(f"Consumo inválido")