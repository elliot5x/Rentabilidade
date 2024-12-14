
def estatisticas(setores, gastos, ganhos, formatar_valor, dados):
    print("=== Estatísticas dos Setores ===")
    for i in range(len(setores)):
        print(f"\nSetor: {setores[i]}")
        print(f"Gastos: R$ {formatar_valor(gastos[i])}")
        print(f"Ganhos: R$ {formatar_valor(ganhos[i])}")

        # Calculando do lucro / prejuízo
        lucrando = ganhos[i] - gastos[i]

        # Verifica se está no prejuízo
        if lucrando < 0:
            print(f"Perdendo: R$: {formatar_valor(lucrando)}")
        else:
            print(f"Lucrando: R$: {formatar_valor(lucrando)}")

    # TOTAL
    print("\n=== TOTAL ===")
    if all(key in dados for key in ["total_gastos", "total_lucros", "diferenca"]):
        print(f"Gastos Totais: R$ {formatar_valor(dados['total_gastos'])}")
        print(f"Ganhos Totais: R$ {formatar_valor(dados['total_lucros'])}")
        print(f"Lucro Total: R$ {formatar_valor(dados['diferenca'])}")
    else:
        print("Os totais consolidados ainda não estão disponíveis.")

    input("\nPressione Enter para voltar ao menu.")
