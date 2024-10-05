menu = """
[d] Depositar
[s] Sacar 
[e] Extrato
[b] Saldo
[q] Sair

=> """

saldo = 100
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(menu)

    if opcao == "d":
        try:
            valor = float(input("Informe o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito de R$ {valor:.2f}\n"
                print("Depósito realizado com sucesso!\n")
            else:
                print("Erro ao depositar. O valor deve ser maior que zero.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.\n")

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                print("Erro: O valor do saque deve ser maior que zero.\n")
            elif valor > limite:
                print(f"Você pode sacar até R$ {limite:.2f} por vez.\n")
            elif valor > saldo:
                print("Saldo insuficiente para o saque solicitado.\n")
            elif numero_saques >= LIMITE_SAQUES:
                print(f"Você atingiu o limite de {LIMITE_SAQUES} saques diários, volte amanhã.\n")
            else:
                numero_saques += 1
                saldo -= valor
                extrato += f"Saque de R$ {valor:.2f}\n"
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.\n")

    elif opcao == "b":
        print(f"Saldo atual: R$ {saldo:.2f}\n")

    elif opcao == "e":
        print("Extrato da conta:")
        if extrato:
            print(extrato)
        else:
            print("Não foram realizadas movimentações.\n")

    elif opcao == "q":
        print("Encerrando o sistema. Obrigado por usar nosso serviço!")
        break

    else:
        print("Operação inválida. Por favor, selecione uma opção válida.\n")

print(f"Resumo do dia:\n{extrato}")
print(f"Total de saques realizados: {numero_saques}")
print(f"Saldo final: R$ {saldo:.2f}")


# até 10 transações em um dia
# caso o usuário tente fazer uma transação após o limite, informar que ele excedeu
# mostrar no extrato a data e hora das transações