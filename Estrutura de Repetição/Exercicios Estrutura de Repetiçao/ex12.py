soma_salario = 0
soma_filhos = 0
cont = 0
maior_salario = 0
salario_100 = 0

salario = float(input("Digite o salário: "))

while salario >= 0:

    filhos = int(input("Digite o número de filhos: "))

    soma_salario = soma_salario + salario
    soma_filhos = soma_filhos + filhos

    cont = cont + 1

    if salario > maior_salario:
        maior_salario = salario

    if salario <= 100:
        salario_100 = salario_100 + 1

    salario = float(input("Digite o salário: "))

media_salario = soma_salario / cont
media_filhos = soma_filhos / cont
percentual = (salario_100 * 100) / cont

print("Média do salário:", media_salario)
print("Média de filhos:", media_filhos)
print("Maior salário:", maior_salario)
print("Percentual com salário até R$100,00:", percentual, "%")