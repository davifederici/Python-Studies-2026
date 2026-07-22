def main():
    a = int(input("Digite o número de alunos:"))

    soma = 0
    qnt = 0
    maior = 0
    notas = []

    for i in range(a):

        n = float(input(f"Digite a nota do aluno {i + 1}:"))

        while n < 0 or n > 10:
            n = float(input("Digite outro valor:"))

        notas.append(n)
        soma += n

    media = soma / a

    for nota in notas:
        if nota < media:
            qnt += 1

        if nota > maior:
            maior = nota

    print(f"Média da turma:{media:.2f}")
    print("Quantidade abaixo da média", qnt)
    print("Maior nota:", maior)

main()