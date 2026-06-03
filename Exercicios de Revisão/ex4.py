n1 = float(input("Digite uma nota:"))
n2 = float(input("Digite uma nota:"))
n3 = float(input("Digite uma nota:"))
n4 = float(input("Digite uma nota:"))
n5 = float(input("Digite uma nota:"))

if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10 and n3 >= 0  and n3 <= 10 and n4 >= 0 and n4 <= 10 and n5 >= 0 and n5 <= 10:
    media = (n1 + n2 + n3 + n4 + n5)/ 5
    print(f"A média do aluno é:{media}")

    if n1 >= n2 and n1 >= n3 and n1 >= n4 and n1 >= n5:
        print(f"A maior nota é:{n1}")
    elif n2 >= n1 and n2 >= n3 and n2 >= n4 and n2 >= n5:
        print(f"A maior nota é:{n2}")
    elif n3 >= n1 and n3 >= n2 and n3 >= n4 and n3 >= n5:
        print(f"A maior nota é:{n3}")
    elif n4 >= n1 and n4 >= n2 and n4 >= n3 and n4 >= n5:
        print(f"A maior nota é:{n4}")
    elif n5 >= n1 and n5 >= n2 and n5 >= n3 and n5 >= n4:
        print(f"A maior nota é:{n5}")
    else:
        print("\n")

    if n1 <= n2 and n1 <= n3 and n1 <= n4 and n1 <= n5:
        print(f"A menor nota é:{n1}")
    elif n2 <= n1 and n2 <= n3 and n2 <= n4 and n2 <= n5:
        print(f"A menor nota é:{n2}")
    elif n3 <= n1 and n3 <= n2 and n3 <= n4 and n3 <= n5:
        print(f"A menor nota é:{n3}")
    elif n4 <= n1 and n4 <= n2 and n4 <= n3 and n4 <= n5:
        print(f"A menor nota é:{n4}")
    elif n5 <= n1 and n5 <= n2 and n5 <= n3 and n5 <= n4:
        print(f"A menor nota é:{n5}")
    else:
        print("\n")

    if media >= 7:
        print("Aluno Aprovado")
    elif media >= 5 and media <= 6.9:
        print("Aluno em recuperação")
    else:
        print("Aluno reprovado")

else:
    print("Nota inválida!")