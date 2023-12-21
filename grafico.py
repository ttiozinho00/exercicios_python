import matplotlib.pyplot as plt
import numpy as np

# Define a nova função
def f(x):
    return 3**(x - 1)

# Gera valores de x de -2 a 2 com intervalo de 0.1
x = np.arange(-2, 2, 0.2)

# Calcula os valores correspondentes de y usando a nova função f(x)
y = f(x)

# Valores de x para os quais queremos calcular f(x)
x_values = [-2, -1, 0, 1, 2]

# Calcula os valores correspondentes de y para os valores de x dados
y_values = [f(x) for x in x_values]

# Plota o gráfico
plt.figure(figsize=(8, 6))

# Plota a nova função
plt.plot(x, y, label=r'$f(x) = 3^{x-1}$', color='b')

# Plota os pontos
plt.scatter(x_values, y_values, color='red', label='Pontos dados')
for x, y in zip(x_values, y_values):
    plt.text(x, y, f'({x}, {y:.2f})', ha='right')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gráfico da função f(x) = 3^{x-1} e pontos dados')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Define os rótulos e espaçamentos adequados no eixo x
plt.xticks(np.arange(-2, 3, 1))
plt.legend()
plt.grid(True)
plt.show()
