saldo = 0


def ver_saldo():
    return saldo


def depositar(valor):
    global saldo
    saldo += valor


def sacar(valor):
    global saldo
    if valor > saldo:
        return False
    saldo -= valor
    return True
