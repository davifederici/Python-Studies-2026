n1 = float(input("Digite a nota:"))
n2 = float(input("Digite a nota:"))
n3 = float(input("Digite a nota:"))
if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10 and n3 >= 0 and n3 <=10:
    soma = n1 + n2 + n3
    print(f"A soma das notas é:{soma:.2f}")
    media = (n1 + n2 + n3) / 3
    print(f"A média é: {media:.2f}")
    if n1 > n2 and n1 > n3:
        print(f"A maior nota é: {n1:.2f}")
    elif n2 > n1 and n2 > n3:
        print(f"A maior nota é: {n2:.2f}")
    else:
        print(f"A maior nota é: {n3:.2f}")

    if n1 < n2 and n1 < n3:
        print(f"A menor nota é: {n1:.2f}")
    elif n2 < n1 and n2 < n3:
        print(f"A menor nota é: {n2:.2f}")
    else:
        print(f"A menor nota é: {n3:.2f}")
else:
    print("Nota inválida!")