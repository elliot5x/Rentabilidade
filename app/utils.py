from os import system, name

def cls():
    system('cls') if name == 'nt' else system('clear')

def formatar_valor(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
