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

menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls, dados)