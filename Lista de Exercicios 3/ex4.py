a = float(input("Digite a nota:"))
b = float(input("Digite a nota:"))
c = float(input("Digite a nota:"))
media = ((a*3) + (b*3) + (c*4))/10
n = 0

if media >= 7:
    print("Aprovado!!!")
    print(f"A média foi de: {media} pontos")
else:
    print("Deverá realizar prova final!!")
    print(f"A sua nota foi de:{media} pontos")
    n = 10 - media
    print(f"Você precisa tirar {n} para passar")
    d = float(input("Digite a nota:"))
    notafinal = (media + d)/2
    if notafinal > 5:
        print("Aprovado!!!")
        print(f"Sua média final foi de:{notafinal} pontos")
    else:
        print("Reprovado!!!")
        print(f"Sua média final foi de:{notafinal} pontos")