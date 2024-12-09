import numpy as np
import matplotlib.pyplot as plt

def analise(setores, gastos, ganhos, formatar_valor, dados):
    while True:
        gastos = [float(g) for g in gastos]
        ganhos = [float(g) for g in ganhos]
        
        total_gastos = sum(gastos)
        total_ganhos = sum(ganhos)
        diferenca = total_ganhos - total_gastos

        if diferenca >= 0:
            status_empresa = "A empresa está indo bem."
        else:
            status_empresa = "A empresa está em prejuízo."

        print("\n=== Análise Geral da Empresa ===")
        print(status_empresa)
        
        maior_prejuizo_valor = float('inf')
        setor_com_maior_prejuizo = ""
        
        for i, setor in enumerate(setores):
            lucro_setor = ganhos[i] - gastos[i]
            if lucro_setor < maior_prejuizo_valor:
                maior_prejuizo_valor = lucro_setor
                setor_com_maior_prejuizo = setor

        melhor_percentual = 0
        melhor_corte = 0
        percentuais = np.linspace(0, 1, 101)

        for percentual in percentuais:
            corte = abs(maior_prejuizo_valor) * percentual
            
            if (total_gastos - corte) <= total_ganhos:
                melhor_percentual = percentual
                melhor_corte = corte
                break
        
        print(f"O setor com maior impacto negativo é: {setor_com_maior_prejuizo}")
        print(f"Recomendação: Cortar R$ {formatar_valor(melhor_corte)} ({melhor_percentual * 100:.0f}%) em gastos no setor {setor_com_maior_prejuizo}.")
        
        setores_bem_sucedidos = []
        setores_com_lucro = []

        for i, setor in enumerate(setores):
            if ganhos[i] > gastos[i]:
                setores_bem_sucedidos.append(setor)
                setores_com_lucro.append((setor, ganhos[i] - gastos[i]))
        
        setores_com_lucro = sorted(setores_com_lucro, key=lambda x: x[1], reverse=True)

        if setores_com_lucro:
            print("\n=== Sugestão de Realocação de Gastos ===")
            for setor, lucro in setores_com_lucro:
                percentual_realocacao = min(0.2, melhor_percentual)  # Transferir no máximo 20%
                gasto_realocado = melhor_corte * percentual_realocacao

                # Atualizando os valores de gastos para refletir a realocação
                index_setor_mal_sucedido = setores.index(setor_com_maior_prejuizo)
                index_setor_bem_sucedido = setores.index(setor)
                
                gastos[index_setor_mal_sucedido] -= gasto_realocado
                gastos[index_setor_bem_sucedido] += gasto_realocado

                print(f"Transferir R$ {formatar_valor(gasto_realocado)} do setor {setor_com_maior_prejuizo} para o setor {setor}.")
                print(f"Novo gasto sugerido para o setor {setor_com_maior_prejuizo}: R$ {formatar_valor(gastos[index_setor_mal_sucedido])}.")
                print(f"Novo gasto sugerido para o setor {setor}: R$ {formatar_valor(gastos[index_setor_bem_sucedido])}.")
        else:
            print("\nNão há setores com lucro suficiente para realocação.")
        
        return
