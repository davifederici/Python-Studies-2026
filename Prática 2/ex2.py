x = int(input("Digite um número:"))
if x % 2 == 0:
    print(f"{x} é par")
else:
    print(f"{x} é ímpar")
if x % 2 == 0 or x % 3 == 0:
    print(f"{x} é divisivel por 2 e 3 ")
if x %2  == 0 and x % 5 == 0:
    print(f"{x} é divisivel por 2 e 5")