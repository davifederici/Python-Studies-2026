d = int(input("Digite o número de dias:"))
km = float(input("Digite os km percorridos:"))
t = int(input("Digite um dos 3 tipos de carro:"))

if d > 0 and km > 0:
    if t == 1:
        diaria = 90 * d
        if km/ d > 100:
            valor = diaria + (km * 0.35)
            print (f"O valor a ser pago é: R$ {valor:.2f}")
        else:
            valor = diaria + (km * 0.20)
            print (f"O valor a ser pago é: R$ {valor:.2f}")

    elif t ==2:
        diaria = 150 * d
        if km /d > 120:
            valor = diaria + (km * 0.45)
            print (f"O valor a ser pago é: R$ {valor:.2f}")
        else:
            valor = diaria + (km * 0.30)
            print (f"O valor a ser pago é: R$ {valor:.2f}")
    elif t == 3:
        diaria = 250 * d
        if km / d > 150:
            valor = diaria + (km * 0.80)
            print(f"O valor a ser pago é: R$ {valor:.2f}")
        else:
            valor = diaria + (km * 0.50)
            print(f"O valor a ser pago é: R$ {valor:.2f}")
    else:
        print("Dados Inválidos")
else:
    print("Dados Inválidos")
