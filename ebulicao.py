import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tk import tkinter as tk

# Função para atualizar o gráfico
def atualizar_grafico():
    # Parâmetros
    volume_ml = int(volume_entry.get())
    num_simulacoes = 1000

    media_variacao = float(media_variacao_entry.get())
    desvio_padrao_variacao = float(desvio_variacao_entry.get())
    media_ebulicao = float(media_ebulicao_entry.get())
    desvio_padrao_ebulicao = float(desvio_ebulicao_entry.get())

    # Ponto mais alto e mais baixo, ponto mais quente e mais frio
    ponto_mais_alto = float(ponto_mais_alto_entry.get())
    ponto_mais_baixo = float(ponto_mais_baixo_entry.get())
    ponto_mais_quente = float(ponto_mais_quente_entry.get())
    ponto_mais_frio = float(ponto_mais_frio_entry.get())

    # Simulação Monte Carlo
    pontos_variacao = np.random.normal(media_variacao, desvio_padrao_variacao, num_simulacoes)
    pontos_ebulicao = np.random.normal(media_ebulicao, desvio_padrao_ebulicao, num_simulacoes)
    variacao_temperatura = pontos_ebulicao - pontos_variacao

    # Filtra os pontos baseados nos critérios
    pontos_filtrados = []
    for i in range(num_simulacoes):
        if ponto_mais_alto <= pontos_variacao[i] <= ponto_mais_baixo and ponto_mais_quente <= pontos_ebulicao[i] <= ponto_mais_frio:
            pontos_filtrados.append((pontos_variacao[i], pontos_ebulicao[i]))

    pontos_variacao_filtrados, pontos_ebulicao_filtrados = zip(*pontos_filtrados)

    # Limpa o gráfico anterior
    ax.clear()

    # Plota o novo gráfico de Monte Carlo
    ax.scatter(pontos_variacao_filtrados, pontos_ebulicao_filtrados, c=variacao_temperatura, cmap='viridis')
    ax.set_xlabel('Ponto de Variação (°C)')
    ax.set_ylabel('Ponto de Ebulição (°C)')
    ax.set_title(f'Simulação Monte Carlo para {volume_ml} ml de Vinho Tinto')
    ax.grid(True)

    # Atualiza o canvas
    canvas.draw()

# Configuração da interface gráfica
root = tk.Tk()
root.title("Simulação Monte Carlo")

# Entradas para os parâmetros
# ... (entradas anteriores)

# Entradas para os pontos mais alto, baixo, quente e frio
tk.Label(root, text="Ponto Mais Alto (°C):").pack()
ponto_mais_alto_entry = tk.Entry(root)
ponto_mais_alto_entry.pack()

tk.Label(root, text="Ponto Mais Baixo (°C):").pack()
ponto_mais_baixo_entry = tk.Entry(root)
ponto_mais_baixo_entry.pack()

tk.Label(root, text="Ponto Mais Quente (°C):").pack()
ponto_mais_quente_entry = tk.Entry(root)
ponto_mais_quente_entry.pack()

tk.Label(root, text="Ponto Mais Frio (°C):").pack()
ponto_mais_frio_entry = tk.Entry(root)
ponto_mais_frio_entry.pack()

# Botão para atualizar o gráfico
atualizar_button = tk.Button(root, text="Atualizar Gráfico", command=atualizar_grafico)
atualizar_button.pack()

# Configuração do gráfico
fig, ax = plt.subplots(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
widget_canvas = canvas.get_tk_widget()
widget_canvas.pack()

# Inicia a interface gráfica
tk.mainloop()


