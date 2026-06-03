p1 = float(input("Digite o valor do produto:"))
p2 = float(input("Digite o valor do produto:"))
p3 = float(input("Digite o valor do produto:"))

valor = p1 + p2 + p3
if valor > 1000:
    valor1 = valor * 0.80
    print(f"O valor ficou de:{valor1}")
elif valor > 500 and valor < 1000:
    valor2 = valor * 0.90
    print(f"O valor ficou de:{valor2}")
else:
    print(f"O valor ficou de:{valor}")