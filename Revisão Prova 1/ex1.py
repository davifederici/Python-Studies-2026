d = float(input("Digite sua distância:"))
if d < 0:
    print("Distância inválida!")
elif d <= 10:
    valor = d * 2.50
    print(f"O valor é de:{valor}")
elif d > 10 and d < 30:
    valor1 = d * 2.00
    print(f"O valor é de:{valor1}")
else:
    valor2 = d * 1.50
    print(f"O valor é de:{valor2}")