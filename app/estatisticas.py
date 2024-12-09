
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
    print(f"Gastos Totais: R$ {formatar_valor(dados["total_gastos"])}")
    print(f"Ganhos Total: R$ {formatar_valor(dados["total_lucros"])}")
    print(f"Lucrando: R$ {formatar_valor(dados["diferenca"])}")

    input("Pressione Enter para voltar ao menu.")
