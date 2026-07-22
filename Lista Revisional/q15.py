def main():
#quantidade de alunos
    a = int(input("Digite o número de alunos:"))

#contador soma
    soma = 0
    qnt = 0
    nota = []
#estrutura de repetição 
    for i in range(a):

        n = float(input(f"Digite a nota do aluno {i + 1}:"))

#estrtura de repetição caso aconteça uma nota inválida
        while n < 0 or n > 10:
            n = float(input("Digite um valor entre 0 e 10:"))

        nota.append(n)
#calculo para soma de notas
        soma += n

#calculo da média
        media = soma / a

    for notas in nota:
        if nota >= media :
            qnt += 1

    print(f"Média das notas: {media:.2f}")
    print("Os alunos com nota maior ou igual a media são:", qnt)
        
main()