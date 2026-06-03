l = int(input("Digite a linha:"))
c = int(input("Digite a coluna:"))

if l >= 1 and l <= 1000 and l >= 1 and l <= 100 :

    if l % 2 == 0 and c % 2 == 1:
        print("0")
    else:
        print("1")