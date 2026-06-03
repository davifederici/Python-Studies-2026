t1 = int(input("Digite a temperatura:"))
t2 = int(input("Digite a temperatura:"))
t3 = int(input("Digite a temperatura:"))
t4 = int(input("Digite a temperatura:"))

if t1 >= -3 and t1 <= 47 and t2 >= -3 and t2 <= 47 and t3 >= -3 and t3 <= 47 and t4 >=-3 and t4 <= 47:
    soma = t1 + t2 + t3 + t4
    print(f"A soma das temperaturas é:{soma}")
    media = (t1 + t2 + t3 + t4)/4
    print(f"A média das temperaturas é:{media}")

    if t1 > t2 and t1 > t3 and t1 > t4:
        print(f"A maior temperatura é:{t1}")
    elif t2 > t1 and t2 > t3 and t2 > t4:
        print(f"A maior temperatura é:{t2}")
    elif t3 > t1 and t3 > t2 and t3 > t4:
        print(f"A maior temperatura é:{t3}")
    elif t4 > t1 and t4 > t2 and t4 > t3:
        print(f"A maior temperatura é:{t4}")
    else:
        print("\n")

    if t1 < t2 and t1 < t3 and t1 < t4:
        print(f"A menor temperatura é:{t1}")
    elif t2 < t1 and t2 < t3 and t2 < t4:
        print(f"A menor temperatura é:{t2}")
    elif t3 < t1 and t3 < t2 and t3 < t4:
        print(f"A menor temperatura é:{t3}")
    elif t4 < t1 and t4 < t2 and t4 < t3:
        print(f"A menor temperatura é:{t4}")
    else:
        print("\n")
    if t1 == t2 and t1 == t3 and t1 == t4:
        print(f"Os valores das temperaturas iguais")
else:
    print("Temperatura inválida!")