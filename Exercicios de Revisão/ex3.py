c = float(input("Digite o valor da compra:"))
t = float(input("Digite a sua categoria:"))
if t == 1:
    print("\n---CLIENTE COMUM---\n")
    if c > 300:
        d = c * 0.05
        valor = c * 0.95
        print(f"O valor original era de: {c}")
        print(f"O desconto aplicado foi de:{d}")
        print(f"O valor final da compra é:{valor}")
    else:
        print(f"O valor original foi de:{c}")
        print("Não teve desconto!")
elif t == 2:
    print("\n---CLIENTE PREMIUM---\n")
    if c > 300:
        d = c * 0.10
        valor2 = c * 0.90
        print(f"O valor original foi de:{c}")
        print(f"O desconto aplicado foi de:{d}")
        print(f"O valor final foi de:{valor2}")
    else:
        print(f"O valor original foi de:{c}")
        print("Não teve desconto!")
elif t == 3:
    print("\n---CLIENTE VIP---\n")
    if c > 300:
        d = c * 0.15
        valor3 = c * 0.85
        print(f"O valor original é:{c}")
        print(f"O desconto aplicado foi de:{d}")
        print(f"O valor final foi de:{valor3}")
    else:
        print(f"O valor original foi de:{c}")
        print("Não teve desconto!")
else:
    print("Tipo de cliente inválido!")