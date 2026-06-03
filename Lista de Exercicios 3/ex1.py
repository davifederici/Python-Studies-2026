a = float(input("Digite a nota da primeira prova:"))
b = float(input("Digite a nota da segunda prova:"))
fal = int(input("Digite quantas faltas:"))
media = (a + b)/2
nota = 0

if media >= 5:
    if fal <=6:
        print("Aprovado!!!")
        print(f"Sua média foi de:{media} pontos")
    else:
        print("Reprovado por falta!")
else:
    print("Reprovado por nota!")
    nota =  5 - media
    print(f"Você ficou reprovado por:{nota} pontos")