from os import system, name


def cls():
    system('cls') if name == 'nt' else system('clear')
cls()

input("Aperte Enter para confirmar...")
