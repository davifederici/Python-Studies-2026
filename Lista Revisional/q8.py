x = 50

a = int(input("Digite o primeiro número:"))

maior = a
menor = a

for i in range(1,x):

    a = int(input(f"Digite o número {i + 1}:"))

    if a > maior:
        maior = a
    
    if a < menor:
        menor = a

print("O maior é:",maior)
print("O menor é:",menor)