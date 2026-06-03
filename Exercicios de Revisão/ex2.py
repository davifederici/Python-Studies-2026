v1 = float(input("Digite o valor das vendas:"))
v2 = float(input("Digite o valor das vendas:"))
v3 = float(input("Digite o valor das vendas:"))
v4 = float(input("Digite o valor das vendas:"))

if v1 >= 0 and v1 <= 50000 and v2 >= 0 and v2 <= 50000 and v3 >= 0 and v3 <= 50000 and v4 >= 0 and v4 <= 50000:
    total = v1 + v2 + v3 + v4
    print(f"O valor total das vendas é de:{total}")

    media = total/4
    print(f"A média semanal de vendas foi de:{media}")

    if v1 >= v2 and v1 >= v3 and v1 >= v4:
        print(f"A maior venda foi:{v1}")
    elif v2 >= v1 and v2 >= v3 and v2 >= v4:
        print(f"A maior venda foi:{v2}")
    elif v3 >= v1 and v3 >= v2 and v3 >= v4:
        print(f"A maior venda foi:{v3}")
    elif v4 >= v1 and v4 >= v2 and v4 >= v3:
        print(f"A maior venda foi:{v4}")
    else:
        print("\n")
    
    if v1 <= v2 and v1 <= v3 and v1 <= v4:
        print(f"A menor venda foi de:{v1}")
    elif v2 <= v1 and v2 <= v3 and v2 <= v4:
        print(f"A menor venda foi de:{v2}")
    elif v3 <= v1 and v3 <= v2 and v3 <= v4:
        print(f"A menor venda foi de:{v3}")
    elif v4 <= v1 and v4 <= v2 and v4 <= v3:
        print(f"A menor venda foi de:{v4}")
    else:
        print("\n")
    
    if media >= 20000:
        print("Meta atingida!")
    else:
        print("Meta não atingida!")
else:
    print("Valor de venda inválido")
    