renda = int(input("Digite a sua renda mensal:"))
valor = 0
if renda < 2259.21:
    print(f"Isento de imposto, salário de:{renda}")

elif renda > 2259.21 and renda <= 2828.65:
    valor = renda * (7.5/100)
    print(f"O salário após o imposta é de:{valor}")

elif renda > 2828.65 and renda <= 3751.05:
    valor = renda * (15/100)
    print(f"O salário após o imposto é de:{valor}")

elif renda > 3751.05 and renda <= 4664.64:
    valor = renda * (22.5/100)
    print(f"O salário após o imposta é de:{valor}")

else:
    valor = renda * (27.5/100)
    print(f"O salário após o imposta é de:{valor}")