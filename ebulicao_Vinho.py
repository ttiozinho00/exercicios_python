import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
volume_ml = 150  # Volume de vinho tinto em ml
num_simulacoes = 1000  # Número de simulações Monte Carlo

# Distribuições para ponto de variação e ebulição do vinho tinto (em graus Celsius)
media_variacao = 20
desvio_padrao_variacao = 2
media_ebulicao = 78
desvio_padrao_ebulicao = 3

# Simulação Monte Carlo
pontos_variacao = np.random.normal(media_variacao, desvio_padrao_variacao, num_simulacoes)
pontos_ebulicao = np.random.normal(media_ebulicao, desvio_padrao_ebulicao, num_simulacoes)

# Calcula a variação da temperatura (ponto de ebulição - ponto de variação)
variacao_temperatura = pontos_ebulicao - pontos_variacao

# Plota o gráfico de Monte Carlo
plt.figure(figsize=(10, 6))
plt.scatter(pontos_variacao, pontos_ebulicao, c=variacao_temperatura, cmap='viridis')
plt.colorbar(label='Variação de Temperatura (°C)')
plt.xlabel('Ponto de Variação (°C)')
plt.ylabel('Ponto de Ebulição (°C)')
plt.title(f'Simulação Monte Carlo para 150 ml de Vinho Tinto')
plt.grid(True)
plt.show()
