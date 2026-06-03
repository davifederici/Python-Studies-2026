soma_antigo = 0
soma_novo = 0
cont = 0

codigo = int(input("Digite o código do produto: "))

while codigo >= 0:

    preco = float(input("Digite o preço do produto: "))

    novo_preco = preco * 1.20

    print("Código do produto:", codigo)
    print("Novo preço: R$", novo_preco)

    soma_antigo = soma_antigo + preco
    soma_novo = soma_novo + novo_preco

    cont = cont + 1

    codigo = int(input("Digite o código do produto: "))

media_antigo = soma_antigo / cont
media_novo = soma_novo / cont

print("Média dos preços sem aumento:", media_antigo)
print("Média dos preços com aumento:", media_novo)