import numpy as np
import matplotlib.pyplot as plt

# Parâmetros
volume_ml = 100  # Volume de água em ml
massa_NaCl_g = 5  # Massa de NaCl em gramas
num_simulacoes = 1000  # Número de simulações Monte Carlo

# Distribuições para ponto de variação e ebulição da solução (em graus Celsius)
media_variacao = 20
desvio_padrao_variacao = 1
media_ebulicao = 100
desvio_padrao_ebulicao = 2

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
plt.title(f'Simulação Monte Carlo para Solução de 5g de NaCl em 100 ml de Água')
plt.grid(True)
plt.show()
