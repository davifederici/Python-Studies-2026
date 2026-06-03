A = float(input("Digite um número:"))
B = float(input("Digite um número:"))
C = float(input("Digite um número:"))

media = (A + B + C) / 3.0

if media >= 9.0:
    print("A")
elif media >= 8.0:
    print("B")
elif media >= 7.0:
    print("C")
elif media >= 6.0:
    print("D")
else:
    print("R")