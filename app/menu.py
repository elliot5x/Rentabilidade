# app/menu.py
from time import sleep
from testes.testes import analise

def menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls, dados):
    while True:
        try:
            cls()
            print("=== RENTABILIDADE EMPRESARIAL ===")
            print("[1] Adicionar\n[2] Estatísticas\n[3] Analise os dados\n[4] Sair")
            digite = int(input("Digite: "))

            if digite == 1:
                cls()
                adicionar(setores, gastos, ganhos, formatar_valor, dados)
            elif digite == 2:
                cls()
                estatisticas(setores, gastos, ganhos, formatar_valor, dados)
            elif digite == 3:
                if len(setores) > 0:
                    try:
                        analise(setores, gastos, ganhos, formatar_valor, dados)
                        input("\nAperte Enter para voltar ao menu.")
                    except Exception as e:
                        print(f"\nOcorreu um erro durante a análise: {e}")
                        input("\nAperte Enter para voltar ao menu.")
                else:
                    input("\nSem análises no momento.\nAperte Enter para voltar ao menu.")

            elif digite == 4:
                exit()
            else:
                print("Escolha um número válido.")
                sleep(2)
                cls()
        except ValueError as ve:
            print(f"Erro: {ve}. Digite apenas números válidos.")
            input("Enter para continuar.")
            cls()
