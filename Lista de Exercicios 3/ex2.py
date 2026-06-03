categoria = int(input("Digite a categoria do produto:"))
preco = 0

if categoria == 1:
    preco = 5
elif categoria == 2:
     preco = 10
elif categoria == 3:
    preco = 23
elif categoria == 4:
    preco = 37
elif categoria == 5:
    preco = 50
else:
    print("Número inválido!")

print(f"Seu preço é: R$ {preco}")