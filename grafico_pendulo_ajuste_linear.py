import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados do experimento (incluídos diretamente para portabilidade do código)
data = {
    'L (Comp. do Fio) Metros': [1.00, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10],
    'T(Período) Segundos': [2.04, 1.92, 1.80, 1.66, 1.54, 1.47, 1.34, 1.11, 0.96, 0.70]
}
df = pd.DataFrame(data)

# Etapa 1: Calcular o quadrado do período
df['T^2'] = df['T(Período) Segundos']**2

# Etapa 2: Realizar a regressão linear para encontrar a melhor reta
# A função np.polyfit retorna o coeficiente angular (slope) e o intercepto (intercept)
slope, intercept = np.polyfit(df['L (Comp. do Fio) Metros'], df['T^2'], 1)

# Cria os pontos para a reta de ajuste (para garantir uma linha contínua)
x_line = np.array([0, 1.0])
y_line = slope * x_line + intercept


# --- Etapa 3: Geração do Gráfico ---
plt.figure(figsize=(10, 7))

# Plota os dados experimentais como um gráfico de dispersão (pontos)
plt.scatter(df['L (Comp. do Fio) Metros'], df['T^2'], color='blue', zorder=5, label='Dados Experimentais ($L, T^2$)')

# Plota a reta de melhor ajuste
plt.plot(x_line, y_line, color='red', label=f'Ajuste Linear (y={slope:.2f}x + {intercept:.2f})')

# Define o título e os rótulos dos eixos
plt.title('Análise do Pêndulo: Período ao Quadrado vs. Comprimento do Fio', fontsize=16)
plt.xlabel('L (Comprimento do Fio) em metros', fontsize=12)
plt.ylabel('$T^2$ (Período ao Quadrado) em $s^2$', fontsize=12)

# Define as marcações (ticks) específicas para os eixos X e Y, conforme solicitado
x_ticks = np.arange(0, 1.1, 0.1)
y_ticks = np.arange(0, 5.0, 0.5)
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# Define os limites dos eixos para um bom enquadramento
plt.xlim(0, 1.05)
plt.ylim(0, 4.55)

# Adiciona uma grade para facilitar a leitura dos valores
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona a legenda para identificar os elementos do gráfico
plt.legend()

# Salva o gráfico em um arquivo de imagem
plt.savefig('grafico_pendulo_ajuste_linear.png')

# Imprime informações no console
print("Gráfico 'grafico_pendulo_ajuste_linear.png' gerado com sucesso.")
print(f"Equação da reta: y = {slope:.4f}x + {intercept:.4f}")

# Se estiver usando um ambiente como Jupyter, descomente a linha abaixo para mostrar o gráfico
# plt.show()
