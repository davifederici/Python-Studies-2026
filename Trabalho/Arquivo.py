from os import system, name

def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def telaAbertura():
    print("Seja bem-vindo")
    input("Pressione Enter para continuar...")

def leValor(funcaoConversao, msgInput="", msgErro="ERRO: Valor inválido"):
    try:
        return funcaoConversao(input(msgInput))
    except:
        print(msgErro)
        return leValor(funcaoConversao, msgInput, msgErro)

def deposito(saldo, estoque):
    limpaTela()

    print("Depósito de notas")
    print("(apenas R$1, R$2, R$5, R$10, R$20, R$50 e R$100)")

    qtd_100 = leValor(int, "Quantidade de notas de R$100: ")
    qtd_50 = leValor(int, "Quantidade de notas de R$50: ")
    qtd_20 = leValor(int, "Quantidade de notas de R$20: ")
    qtd_10 = leValor(int, "Quantidade de notas de R$10: ")
    qtd_5 = leValor(int, "Quantidade de notas de R$5: ")
    qtd_2 = leValor(int, "Quantidade de notas de R$2: ")
    qtd_1 = leValor(int, "Quantidade de notas de R$1: ")

    valor = (
        qtd_100 * 100 +
        qtd_50 * 50 +
        qtd_20 * 20 +
        qtd_10 * 10 +
        qtd_5 * 5 +
        qtd_2 * 2 +
        qtd_1 * 1
    )

    if valor > 0:
        saldo += valor

        estoque[100] += qtd_100
        estoque[50] += qtd_50
        estoque[20] += qtd_20
        estoque[10] += qtd_10
        estoque[5] += qtd_5
        estoque[2] += qtd_2
        estoque[1] += qtd_1

        print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("Nenhuma nota foi depositada.")

    input("\nPressione Enter para continuar...")
    return saldo, estoque

def saque(saldo, estoque):
    limpaTela()

    print("----------------------------------")
    print("Notas disponíveis na máquina:")
    print(f"Notas de R$100: {estoque[100]}")
    print(f"Notas de R$50 : {estoque[50]}")
    print(f"Notas de R$20 : {estoque[20]}")
    print(f"Notas de R$10 : {estoque[10]}")
    print(f"Notas de R$5  : {estoque[5]}")
    print(f"Notas de R$2  : {estoque[2]}")
    print(f"Notas de R$1  : {estoque[1]}")
    print("----------------------------------")

    valor = leValor(int, "Digite o valor a ser sacado: R$ ")

    if valor > 0:
        if valor <= saldo:
            saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente.")
    else:
        print("O valor do saque deve ser positivo.")

    input("\nPressione Enter para continuar...")
    return saldo, estoque

def exibirEstoque(estoque):
    limpaTela()

    print("Estoque de notas no caixa:")
    print(f"Notas de R$100: {estoque[100]}")
    print(f"Notas de R$50 : {estoque[50]}")
    print(f"Notas de R$20 : {estoque[20]}")
    print(f"Notas de R$10 : {estoque[10]}")
    print(f"Notas de R$5  : {estoque[5]}")
    print(f"Notas de R$2  : {estoque[2]}")
    print(f"Notas de R$1  : {estoque[1]}")

    input("\nPressione Enter para continuar...")

def caixaEletronico(saldo=0, estoque=None):

    if estoque is None:
        estoque = {
            100: 0,
            50: 0,
            20: 0,
            10: 0,
            5: 0,
            2: 0,
            1: 0
        }

    limpaTela()

    print("--------------------------")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("4 - Relatório")
    print("5 - Finalizar")
    print("--------------------------")

    opcao = leValor(
        int,
        "Digite uma opção: ",
        "A opção deve ser um número inteiro."
    )

    if opcao == 1:
        saldo, estoque = deposito(saldo, estoque)
        caixaEletronico(saldo, estoque)

    elif opcao == 2:
        saldo, estoque = saque(saldo, estoque)
        caixaEletronico(saldo, estoque)

    elif opcao == 3:
        limpaTela()
        print(f"Saldo atual: R${saldo:.2f}")
        input("\nPressione Enter para continuar...")
        caixaEletronico(saldo, estoque)

    elif opcao == 4:
        exibirEstoque(estoque)
        caixaEletronico(saldo, estoque)

    elif opcao == 5:
        print("Finalizando...")
        print("Obrigado por usar nosso caixa eletrônico!")
        exit()

    else:
        print("Opção inválida!")
        input("Pressione Enter para continuar...")
        caixaEletronico(saldo, estoque)

def main():
    limpaTela()
    telaAbertura()
    caixaEletronico()

main()