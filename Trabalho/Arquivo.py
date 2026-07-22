"""
Trabalho: Cofrinho Digital
Alunos: Davi Federici Mendes Soares
"""



from os import system, name

def limpaTela():
    """
    Limpa a tela do terminal independentemente do sistema operacional.
    Utiliza 'cls' para sistemas baseados em Windows (NT) e 'clear' para Unix/Linux/Mac.
    """
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def telaAbertura():
    """
    Exibe a mensagem de boas-vindas inicial e aguarda a interação do usuário
    para prosseguir com a execução do programa.
    """
    print("Seja bem-vindo")
    input("Pressione Enter para continuar...")

def leValor(funcaoConversao, msgInput="", msgErro="ERRO: Valor inválido"):
    """
    Solicita uma entrada do usuário e tenta convertê-la para um tipo específico.
    Se a conversão falhar, exibe uma mensagem de erro e pede a entrada novamente (recursão).

    Parâmetros:
    funcaoConversao (type): O tipo de dado esperado (ex: int, float).
    msgInput (str): A mensagem que será exibida no prompt de entrada.
    msgErro (str): A mensagem exibida caso o usuário digite um valor inválido.

    Retorna:
    O valor digitado pelo usuário convertido para o tipo especificado.
    """
    try:
        return funcaoConversao(input(msgInput))
    except:
        print(msgErro)
        return leValor(funcaoConversao, msgInput, msgErro)

def deposito(saldo, estoque):
    """
    Realiza o depósito de notas no cofrinho digital.
    Pede ao usuário a quantidade de cada nota inserida, calcula o valor total,
    adiciona ao saldo atual e atualiza o estoque físico da máquina.

    Parâmetros:
    saldo (float/int): O saldo atual disponível na conta do usuário.
    estoque (dict): Dicionário contendo a quantidade atual de cada nota na máquina.

    Retorna:
    A atualização do saldo depois do depósito
    """
    limpaTela()

    print("Depósito de notas")
    print("(apenas R$1, R$2, R$5, R$10, R$20, R$50 e R$100)")

    qtd_100 = leValor(int, "Quantidade de notas de R$100: ")
    while qtd_100 < 0:
        qtd_100 = leValor(int, "Quantidade de notas de R$100: ")

    qtd_50 = leValor(int, "Quantidade de notas de R$50: ")
    while qtd_50 < 0:
        qtd_50 = leValor(int, "Quantidade de notas de R$50: ")

    qtd_20 = leValor(int, "Quantidade de notas de R$20: ")
    while qtd_20 < 0:
        qtd_20 = leValor(int, "Quantidade de notas de R$20: ")

    qtd_10 = leValor(int, "Quantidade de notas de R$10: ")
    while qtd_10 < 0:
        qtd_10 = leValor(int, "Quantidade de notas de R$10: ")

    qtd_5 = leValor(int, "Quantidade de notas de R$5: ")
    while qtd_5 < 0:
        qtd_5 = leValor(int, "Quantidade de notas de R$5: ")

    qtd_2 = leValor(int, "Quantidade de notas de R$2: ")
    while qtd_2 < 0:
        qtd_2 = leValor(int, "Quantidade de notas de R$2: ")

    qtd_1 = leValor(int, "Quantidade de notas de R$1: ")
    while qtd_1 < 0:
        qtd_1 = leValor(int, "Quantidade de notas de R$1: ")

    valor = (
        qtd_100 * 100 +
        qtd_50 * 50 +
        qtd_20 * 20 +
        qtd_10 * 10 +
        qtd_5 * 5 +
        qtd_2 * 2 +
        qtd_1
    )

    if valor == 0:
        print("Nenhuma nota foi depositada.")
    else:
        saldo += valor

        estoque[100] += qtd_100
        estoque[50] += qtd_50
        estoque[20] += qtd_20
        estoque[10] += qtd_10
        estoque[5] += qtd_5
        estoque[2] += qtd_2
        estoque[1] += qtd_1

        print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")

    input("\nPressione Enter para continuar...")
    return saldo

def saque(saldo, estoque):
    """
    Realiza o processo de saque, validando o saldo do usuário e a disponibilidade
    de notas no estoque físico da máquina. Utiliza um algoritmo guloso para priorizar
    a entrega de notas de maior valor.

    Parâmetros:
    saldo (float/int): O saldo atual na conta do usuário.
    estoque (dict): Dicionário contendo as notas disponíveis na máquina.

    Retorna:
    Atualização do saldo após o saque
    """
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

    valor = leValor(int, "Digite o valor do saque: R$ ")

    if valor <= 0:
        print("Valor inválido.")
        input("\nPressione Enter para continuar...")
        return saldo

    if valor > saldo:
        print(f"\nSaldo disponível: R${saldo:.2f}")
        op = input("Deseja sacar todo o saldo? (S/N): ").upper()

        if op == "S":
            valor = saldo
        else:
            input("\nPressione Enter para continuar...")
            return saldo

    restante = valor

    usa100 = 0
    usa50 = 0
    usa20 = 0
    usa10 = 0
    usa5 = 0
    usa2 = 0
    usa1 = 0

    while restante >= 100 and estoque[100] > usa100:
        restante -= 100
        usa100 += 1

    while restante >= 50 and estoque[50] > usa50:
        restante -= 50
        usa50 += 1

    while restante >= 20 and estoque[20] > usa20:
        restante -= 20
        usa20 += 1

    while restante >= 10 and estoque[10] > usa10:
        restante -= 10
        usa10 += 1

    while restante >= 5 and estoque[5] > usa5:
        restante -= 5
        usa5 += 1

    while restante >= 2 and estoque[2] > usa2:
        restante -= 2
        usa2 += 1

    while restante >= 1 and estoque[1] > usa1:
        restante -= 1
        usa1 += 1

    if restante != 0:
        print("\nNão há notas suficientes para realizar esse saque.")
        input("\nPressione Enter para continuar...")
        return saldo

    saldo -= valor

    estoque[100] -= usa100
    estoque[50] -= usa50
    estoque[20] -= usa20
    estoque[10] -= usa10
    estoque[5] -= usa5
    estoque[2] -= usa2
    estoque[1] -= usa1

    print("\nNotas entregues:")

    while usa100 > 0:
        print("R$100")
        usa100 -= 1

    while usa50 > 0:
        print("R$50")
        usa50 -= 1

    while usa20 > 0:
        print("R$20")
        usa20 -= 1

    while usa10 > 0:
        print("R$10")
        usa10 -= 1

    while usa5 > 0:
        print("R$5")
        usa5 -= 1

    while usa2 > 0:
        print("R$2")
        usa2 -= 1

    while usa1 > 0:
        print("R$1")
        usa1 -= 1

    print(f"\nSaque de R${valor:.2f} realizado com sucesso.")

    input("\nPressione Enter para continuar...")

    return saldo

def exibirEstoque(estoque, saldo):
    """
    Exibe um relatório na tela informando a quantidade exata de cada nota
    no estoque da máquina e o saldo atual disponível.

    Parâmetros:
    estoque (dict): Dicionário com as quantidades de notas.
    saldo (float/int): Valor do saldo da conta.
    """
    limpaTela()

    print("========== RELATÓRIO ==========")
    print(f"Notas de R$100: {estoque[100]}")
    print(f"Notas de R$50 : {estoque[50]}")
    print(f"Notas de R$20 : {estoque[20]}")
    print(f"Notas de R$10 : {estoque[10]}")
    print(f"Notas de R$5  : {estoque[5]}")
    print(f"Notas de R$2  : {estoque[2]}")
    print(f"Notas de R$1  : {estoque[1]}")
    print("-------------------------------")
    print(f"Saldo: R${saldo:.2f}")

    input("\nPressione Enter para continuar...")

def caixaEletronico(saldo=208, estoque=None):
    """
    Gerencia o menu principal e a navegação do sistema de cofrinho digital.
    Utiliza recursão para se manter em execução até que o usuário escolha
    a opção de finalizar (opção 5).

    Parâmetros:
    saldo (float/int): Saldo inicial ao iniciar a máquina (padrão é 208).
    estoque (dict, optional): Dicionário de estoque de notas. Se None, 
                              inicializa com 1 unidade de cada nota.
    """
    if estoque is None:
        estoque = {
            100: 1,
            50: 1,
            20: 2,
            10: 1,
            5: 1,
            2: 1,
            1: 1
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
        saldo = deposito(saldo, estoque)
        caixaEletronico(saldo, estoque)

    elif opcao == 2:
        saldo = saque(saldo, estoque)
        caixaEletronico(saldo, estoque)

    elif opcao == 3:
        limpaTela()
        print(f"Saldo atual: R${saldo:.2f}")
        input("\nPressione Enter para continuar...")
        caixaEletronico(saldo, estoque)

    elif opcao == 4:
        exibirEstoque(estoque, saldo)
        caixaEletronico(saldo, estoque)

    elif opcao == 5:
        if saldo > 0:
            print(f"\nAinda existem R${saldo:.2f} no cofrinho.")
            resposta = input("Deseja sacar todo o dinheiro antes de sair? (S/N): ").upper()

            if resposta == "S":
                print("\nNotas entregues:")

                while estoque[100] > 0:
                    print("R$100")
                    estoque[100] -= 1

                while estoque[50] > 0:
                    print("R$50")
                    estoque[50] -= 1

                while estoque[20] > 0:
                    print("R$20")
                    estoque[20] -= 1

                while estoque[10] > 0:
                    print("R$10")
                    estoque[10] -= 1

                while estoque[5] > 0:
                    print("R$5")
                    estoque[5] -= 1

                while estoque[2] > 0:
                    print("R$2")
                    estoque[2] -= 1

                while estoque[1] > 0:
                    print("R$1")
                    estoque[1] -= 1

                saldo = 0

        print("\nFinalizando...")
        print("Obrigado por usar nosso Cofrinho Digital!")
        exit()

    else:
        print("Opção inválida!")
        input("\nPressione Enter para continuar...")
        caixaEletronico(saldo, estoque)

def main():
    """
    Função principal que inicia o ciclo de vida do programa.
    Limpa a tela, exibe as boas-vindas e chama o menu principal.
    """
    limpaTela()
    telaAbertura()
    caixaEletronico()

# Executa o programa
main()