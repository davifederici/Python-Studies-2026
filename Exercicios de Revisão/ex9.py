n1 = float(input("Digite o valor:"))
n2 = float(input("Digite o valor:"))
n3 = float(input("Digite o valor:"))
n4 = float(input("Digite o valor:"))

soma = n1 + n2 + n3 + n4
if soma <= 1000:
    print(f"O valor é de:{soma}")
elif soma > 1000 and soma <= 2000:
    valor = soma * 0.85
    print(f"O valor será de: {valor:.2f}")
else:
    valor = soma * 0.75
    print(f"O valor será de: R$ {valor:.2f}")