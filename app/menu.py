# app/menu.py
from time import sleep
from testes.testes import analise

def menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls, dados):
    while True:
        try:
            cls()
            print("=== RENTABILIDADE EMPRESARIAL ===")
            print("[1] Adicionar\n[2] Estatísticas\n[3] Analise os dados\n[4] Remover dados\n[5] Sair")
            digite = input("Digite: ").strip().lower()

            if digite == "1" or digite == "adicionar":
                cls()
                adicionar(setores, gastos, ganhos, formatar_valor, dados, menu)
            elif digite == "2" or digite == "estatisticas":
                cls()
                estatisticas(setores, gastos, ganhos, formatar_valor, dados)
            elif digite == "3" or digite == "analise de dados":
                if len(setores) > 0:
                    try:
                        analise(setores, gastos, ganhos, formatar_valor, dados)
                        input("\nAperte Enter para voltar ao menu.")
                    except Exception as e:
                        print(f"\nOcorreu um erro durante a análise: {e}")
                        input("\nAperte Enter para voltar ao menu.")
                else:
                    input("\nSem análises no momento.\nAperte Enter para voltar ao menu.")
            elif digite == "4" or digite == "remover":
                remover(setores, gastos, ganhos, cls, sleep, dados)
            elif digite == "5" or digite == "sair":
                exit()
            else:
                print("Escolha um número válido.")
                sleep(2)
                cls()
        except ValueError as ve:
            print(f"Erro: {ve}. Digite apenas números válidos.")
            input("Enter para continuar.")
            cls()

def remover(setores, gastos, ganhos, cls, sleep, dados):
    while True:
        cls()
        print("Setores Atuais:")
        for i, setor in enumerate(setores):
            print(f"{i + 1}. {setor} (Gastos: {gastos[i]}, Ganhos: {ganhos[i]})")
        print("\n[0] Voltar")
        print("[R] Remover Todos os Setores")
        
        escolha = input("Escolha o número do setor para remover: ").strip().upper()
        try:
            if escolha == "0":
                break
            elif escolha == "R":
                setores.clear()
                gastos.clear()
                ganhos.clear()
                for key in ["total_gastos", "total_lucros", "diferenca"]:
                    if key in dados:
                        dados[key] = 0.0
                print("\nTodos os setores foram removidos!")
                sleep(2)
            elif escolha.isdigit():
                escolha = int(escolha) - 1
                if 0 <= escolha < len(setores):
                    print(f"\nSetor '{setores[escolha]}' removido!")
                    if "total_gastos" in dados:
                        dados["total_gastos"] -= gastos[escolha]
                    if "total_lucros" in dados:
                        dados["total_lucros"] -= ganhos[escolha]
                    if "diferenca" in dados:
                        dados["diferenca"] -= (ganhos[escolha]- gastos[escolha])

                    del setores[escolha]
                    del gastos[escolha]
                    del ganhos[escolha]
                    sleep(2)
                else:
                    print("\nNúmero inválido. Tente novamente.")
                    sleep(2)
            else:
                print("\nOpção inválida. Tente novamente.")
                sleep(2)
        except Exception as e:
            print(f"Erro {e}")