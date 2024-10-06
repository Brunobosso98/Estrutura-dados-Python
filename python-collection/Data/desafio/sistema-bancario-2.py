import datetime

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
numero_transacoes = 0
LIMITE_TRANSACOES = 10

data_hoje = datetime.date.today()
print(data_hoje)

while True:
    data_atual = datetime.date.today()
    
    if data_atual != data_hoje:
        numero_transacoes = 0
        numero_saques = 0
        data_hoje = data_atual
        print("Novo dia iniciado. Contadores de transações e saques foram reiniciados.\n")

    opcao = input(menu)

    if opcao == "d":
        if numero_transacoes >= LIMITE_TRANSACOES:
            print(f"Limite de {LIMITE_TRANSACOES} transações diárias atingido. Tente novamente amanhã.\n")
            continue

        try:
            valor = float(input("Informe o valor a ser depositado: "))
            if valor > 0:
                saldo += valor
                data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                extrato += f"Depósito de R$ {valor:.2f} em {data_hora}\n"
                numero_transacoes += 1
                print("Depósito realizado com sucesso!\n")
            else:
                print("Erro ao depositar. O valor deve ser maior que zero.\n")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.\n")

    elif opcao == "s":
        if numero_transacoes >= LIMITE_TRANSACOES:
            print(f"Limite de {LIMITE_TRANSACOES} transações diárias atingido. Tente novamente amanhã.\n")
            continue

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
                data_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                extrato += f"Saque de R$ {valor:.2f} em {data_hora}\n"
                numero_transacoes += 1
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

print("Resumo do dia:")
print(extrato if extrato else "Nenhuma transação realizada.")
print(f"Total de saques realizados: {numero_saques}")
print(f"Saldo final: R$ {saldo:.2f}")
