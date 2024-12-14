from app.menu import menu
from app.adicionar import adicionar
from app.estatisticas import estatisticas
from app.utils import cls, formatar_valor

# Variáveis globais
setores = []
gastos = []
ganhos = []


# Dados totais
dados = {
    "total_gastos": 0,
    "total_lucros": 0,
    "diferenca": 0
}

def remover(setores, gastos, ganhos, cls, sleep):
    while True:
        cls()
        print("Setores Atuais:")
        for i, setor in enumerate(setores):
            print(f"{i + 1}. {setor} (Gastos: {gastos[i]}, Ganhos: {ganhos[i]})")
        print("\n0. Voltar")
        print("R. Remover Todos os Setores")
        
        escolha = input("Escolha o número do setor para remover ou uma opção: ").strip().upper()
        
        if escolha == "0":
            break
        elif escolha == "R":
            setores.clear()
            gastos.clear()
            ganhos.clear()
            print("Todos os setores foram removidos!")
            sleep(2)
        elif escolha.isdigit():
            escolha = int(escolha) - 1
            if 0 <= escolha < len(setores):
                print(f"Setor '{setores[escolha]}' removido!")
                del setores[escolha]
                del gastos[escolha]
                del ganhos[escolha]
                sleep(2)
            else:
                print("Número inválido. Tente novamente.")
                sleep(2)
        else:
            print("Opção inválida. Tente novamente.")
            sleep(2)


menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls, remover)