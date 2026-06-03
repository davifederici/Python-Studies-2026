l = float(input("Digite o consumo de kWh: "))
tipo = int(input("Digite o tipo (1-Residencial, 2-Comercial, 3-Industrial): "))

r = 1
c = 2
i = 3

if l < 0:
    print("Dados inválidos")

elif tipo == r:

    print("\n---RESIDENCIAL---\n")

    if l <= 150:
        v = l * 0.60

    else:
        v = l * 0.75

    print(f"O consumo foi de: {l}")
    print(f"O valor residencial foi de: {v}")

elif tipo == c:

    print("\n---COMERCIAL---\n")

    if l <= 1000:
        v1 = l * 0.55

    else:
        v1 = l * 0.70

    print(f"O consumo foi de: {l}")
    print(f"O valor comercial é de: {v1}")

elif tipo == i:

    print("\n---INDUSTRIAL---\n")

    if l <= 5000:
        v2 = l * 0.50

    else:
        v2 = l * 0.65

    print(f"O consumo foi de: {l}")
    print(f"O valor industrial é de: {v2}")

else:
    print("Dados inválidos")