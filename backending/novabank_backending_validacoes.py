from cores import Verde, Vermelho, Azul, Reset


def validacoes(opcao, saldo):
    sair = False

    if opcao not in "VSDX":
        print(f"{Vermelho}Termo inválido ❌{Reset}")
        return saldo, sair

    if opcao == "D":
        valor = int(input(f"\n Digite o valor do depósito {Verde}R${Reset} "))
        saldo += valor
        print(f"{Verde}\n Depósito realizado 💸 | {Verde}R${Reset}{saldo}")
    elif opcao == "S":
        valor = int(input(f"\n Digite o valor do saque {Verde}R${Reset} "))
        if valor > saldo:
            print(f"{Vermelho}\n Saldo insuficiente ❌{Reset}")
        else:
            saldo -= valor
            print(f"{Verde}\n Saque realizado 💳 | {Verde}R${Reset}{saldo}")
    elif opcao == "V":
        print(f"{Azul}Saldo atual:{Reset} {Verde}R${Reset}{saldo}")
        
    elif opcao == "X":
        sair = True   
        
    return saldo, sair