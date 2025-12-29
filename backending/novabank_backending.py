from cores import Verde, Magenta, Negrito, Reset,Amarelo
from novabank_backending_validacoes import validacoes


def main():
    saldo = 0

    print(f"{Amarelo}=={Reset}"*20)
    print(f"{Magenta}BEM-VINDO AO NOVABANK🏦🧡🌐{Reset}")
    print(f"{Amarelo}=={Reset}"*20)

    while True:
        opcao = input(f"""
        {Negrito}Qual a sua transação?{Reset}
                V - Ver o Saldo ({Verde}R${Reset})
                S - Sacar o valor ({Verde}R${Reset})
                D - Depositar o valor ({Verde}R${Reset})
                X - Encerrar Programa: """).upper().strip()

        saldo, sair = validacoes(opcao, saldo)

        if sair:
            print(
                f"\n {Magenta}Encerrando o programa 🏦💠💸💳 "
                f"Obrigado por usar NOVABANK! 🐍{Reset}")
            break


if __name__ == "__main__":
    main()