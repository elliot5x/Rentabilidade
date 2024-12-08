from time import sleep
from app.utils import cls

def adicionar(setores, gastos, ganhos, formatar_valor):
    while True:
        cls()
        setor = input("Setor: ").strip()
        if setor.lower() == "sair":
            break
            
        try:
            gasto = float(input("Gastos: R$ ").replace(".", "").replace(",", "."))
            ganho = float(input("Ganhos: R$ ").replace(".", "").replace(",", "."))
        except ValueError:
            print("Erro: Por favor, insira valores numéricos para gastos e lucros no formato correto.")
            sleep(2)
            continue

        setores.append(setor)
        gastos.append(gasto)
        ganhos.append(ganho)

        # Calcula os totais
        total_gastos = sum(gastos)
        total_lucros = sum(ganhos)
        diferenca = total_lucros - total_gastos

        print("\nResumo:")
        print(f"Gastos Totais: R$ {formatar_valor(total_gastos)}")
        print(f"Ganhos Total: R$ {formatar_valor(total_lucros)}")
        print(f"Diferença: R$ {formatar_valor(diferenca)}")

        while True:
            sair = input("\nDeseja adicionar outro setor? (y/n): ").strip().lower()
            if sair == "y":
                break
            elif sair == "n":
                return
            else:
                print("Opção inválida. Digite 'y' para continuar ou 'n' para sair.")
                sleep(2)
