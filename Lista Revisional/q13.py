def calcular_media(n1,n2,n3):

    media = (n1 + n2 + n3) / 3

    return media

def situacao(media):

    if media >= 7:
        return "Aprovado"

    elif media >= 5 and media < 7:
        return "Recuperação"

    else:
        return "Reprovado"

def main():

    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    n3 = float(input("Digite a terceira nota:"))

    if n1 >= 0 and n1 <= 10 and n2 >= 0 and n2 <= 10 and n3 >= 0 and n3 <= 10:
        m = calcular_media(n1,n2,n3)
        print("A média do aluno é:",m)
        print("Situação",situacao(m))

main()