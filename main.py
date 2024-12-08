from app.menu import menu
from app.adicionar import adicionar
from app.estatisticas import estatisticas
from app.utils import cls, formatar_valor

# Variáveis globais
setores = []
gastos = []
ganhos = []

# Chama o menu, passando as funções e variáveis necessárias
menu(setores, gastos, ganhos, adicionar, estatisticas, formatar_valor, cls)
