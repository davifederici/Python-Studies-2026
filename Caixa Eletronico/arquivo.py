from os import system, name

def limpaTela(): 

    if name == 'nt': system('cls') 
    else: system('clear')

def telaAbertura():
     
     print("Seja bem-vindo") 
     input("Pressione uma tecla para continuar...")

def leValor(funcaoConversao, msgInput="", msgErro="ERRO: Valor inválido"): 
    
    try: return funcaoConversao(input(msgInput)) 

    except: print(msgErro) 

    return leValor(funcaoConversao, msgInput, msgErro)

def deposito(saldo, estoque): 

    limpaTela() 

    print("Depósito de notas (apenas R$ 20, R$ 50, R$ 100)")

    qtd_100 = leValor(int, "Quantidade de notas de R$100: ", "Valor inválido")
    qtd_50 = leValor(int, "Quantidade de notas de R$50: ", "Valor inválido")
    qtd_20 = leValor(int, "Quantidade de notas de R$20: ", "Valor inválido")

    valor = (qtd_100 * 100) + (qtd_50 * 50) + (qtd_20 * 20)

    if valor > 0:

        saldo += valor
        estoque[100] += qtd_100
        estoque[50] += qtd_50
        estoque[20] += qtd_20

        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    else:
        print("Nenhuma nota depositada. Tente novamente!")

    input("Pressione Enter para continuar...")

    return saldo, estoque

def saque(saldo, estoque): 

    limpaTela() 

    valor = leValor(float, "Valor a sacar: R$ ", "Valor inválido")

    if valor > 0:
        if valor <= saldo:

            saldo -= valor 
            print(f"Saque de R${valor:.2f} realizado com sucesso.") 

        else: 
            print("Saldo insuficiente.")

    else: print("O valor do saque deve ser positivo.") 

    input("Pressione Enter para continuar...") 

    return saldo, estoque

def exibirEstoque(estoque):
     
     limpaTela()

     print("Estoque de notas no caixa:") 
     print(f"Notas de R$100: {estoque[100]}") 
     print(f"Notas de R$50 : {estoque[50]}") 
     print(f"Notas de R$20 : {estoque[20]}")

     input("Pressione Enter para continuar...")

def caixaEletronico(saldo=0, estoque=None): 

    if estoque is None: estoque = {100: 0, 50: 0, 20: 0}
    
    limpaTela()
    print("===== CAIXA ELETRÔNICO =====")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Saldo")
    print("4 - Estoque de notas")
    print("5 - Sair")

    opcao = leValor(int, "Digite uma opção: ", "A opção deve ser um número inteiro.")

    if opcao == 1:

        saldo, estoque = deposito(saldo, estoque)

        caixaEletronico(saldo, estoque)  # chamada recursiva

    elif opcao == 2:

        saldo, estoque = saque(saldo, estoque)
        caixaEletronico(saldo, estoque)  # chamada recursiva

    elif opcao == 3:

        limpaTela()

        print(f"Saldo atual: R${saldo:.2f}")

        input("Pressione Enter para continuar...")

        caixaEletronico(saldo, estoque)  

    elif opcao == 4:

        exibirEstoque(estoque)
        caixaEletronico(saldo, estoque)  

    elif opcao == 5:

        print("Finalizando... Obrigado por usar nosso caixa eletrônico!")
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