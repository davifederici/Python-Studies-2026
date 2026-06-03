d = int(input("Digite os dias que você foi a academia:"))
if d >= 0 and d <= 31:
    if d <= 8:
        valor = d * 15
        print(f"O valor a pagar é de:{valor}")
    elif d > 8 and d <= 20:
        valor1 = d * 12
        print(f"O valor a pagar é de:{valor1}")
    else:
        valor3 = d * 10
        print(f"O valor a pagar é de:{valor3}")
else:
    print("Quantidade de dias inválida")