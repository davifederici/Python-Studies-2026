a = int(input("Digite um número:"))
b = int(input("Digite um número:"))
c = int(input("Digite um número:"))
if a >= 0 and a <= 100 and b >= 0 and b <= 100 and c >= 0 and c <= 100:
    if a == b:
        print(f"{c}")
    elif a == c:
        print(f"{b}")
    else:
        print(f"{a}")