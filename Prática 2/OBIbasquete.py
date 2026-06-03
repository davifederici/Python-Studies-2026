D = int(input("Digite os metros:"))
if D <= 800:
    print("1 ponto")
elif D > 800 and D <= 1400:
    print("2 pontos")
elif D > 1400 and D <= 2000:
    print("3 pontos")
else:
    print("Tente novamente")