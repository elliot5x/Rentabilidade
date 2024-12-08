# app/menu.py
from time import sleep

def menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls):
    while True:
        try:
            cls()
            print("=== RENTABILIDADE EMPRESARIAL ===")
            print("[1] Adicionar\n[2] Estatísticas\n[3] Sair")
            digite = int(input("Digite: "))

            if digite == 1:
                cls()
                adicionar(setores, gastos, ganhos, formatar_valor)
            elif digite == 2:
                cls()
                estatisticas(setores, gastos, ganhos, formatar_valor)
            elif digite == 3:
                exit()
            else:
                print("Escolha um número válido.")
                sleep(2)
                cls()

        except ValueError:
            print("Digite apenas números válidos.")
            sleep(2)
            cls()
