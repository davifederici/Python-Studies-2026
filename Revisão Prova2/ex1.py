def main():
    x = int(input("Digite o número de alunos:"))

    soma = 0
    cont = 0
    aprovados = 0

    while x > cont:

        num = float(input(f"Digite a bota do aluno{cont + 1}:"))

        while num < 0 or num > 10:
            print("Nota inválida:")
            num = float(input(f"Digite a nota do aluno{cont + 1}:"))

        soma += num

        if num >= 7:
            aprovados += 1

        cont += 1

    media = soma / x

    print(f"Média das notas: {media: .2f}",)
    print("Número de alunos com notas >= 7:", aprovados)

main()