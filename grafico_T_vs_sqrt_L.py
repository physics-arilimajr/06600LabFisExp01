import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados do experimento
data = {
    'L (Comp. do Fio) Metros': [1.00, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10],
    'T(Período) Segundos': [2.04, 1.92, 1.80, 1.66, 1.54, 1.47, 1.34, 1.11, 0.96, 0.70]
}
df = pd.DataFrame(data)

# Etapa 1: Calcular a raiz quadrada do comprimento
df['sqrt_L'] = np.sqrt(df['L (Comp. do Fio) Metros'])

# Etapa 2: Realizar a regressão linear para T em função de sqrt(L)
slope, intercept = np.polyfit(df['sqrt_L'], df['T(Período) Segundos'], 1)

# Etapa 3: Calcular o valor experimental da gravidade
# A equação é T = (2π/√g) * √L. O coeficiente angular (slope) é m = 2π/√g
# Portanto, g = (2π/m)²
g_experimental = (2 * np.pi / slope)**2

# Etapa 4: Comparar com o valor teórico e calcular o erro
g_teorico = 9.807  # m/s²
erro_percentual = (abs(g_experimental - g_teorico) / g_teorico) * 100

# --- Geração do Gráfico T vs. sqrt(L) ---
plt.figure(figsize=(10, 7))

# Plota os dados experimentais
plt.scatter(df['sqrt_L'], df['T(Período) Segundos'], color='green', zorder=5, label='Dados Experimentais (√L, T)')

# Cria os pontos para a reta de ajuste
x_line = np.array([df['sqrt_L'].min(), df['sqrt_L'].max()])
y_line = slope * x_line + intercept

# Plota a reta de melhor ajuste
plt.plot(x_line, y_line, color='purple', linestyle='--', label=f'Ajuste Linear (y={slope:.2f}x + {intercept:.2f})')

# Define o título e os rótulos dos eixos
plt.title('Análise do Pêndulo: Período vs. Raiz Quadrada do Comprimento', fontsize=16)
plt.xlabel('Raiz Quadrada de L (√m)', fontsize=12)
plt.ylabel('T (Período) em segundos', fontsize=12)

# Define as marcações (ticks)
x_ticks = np.arange(0.3, 1.1, 0.1)
y_ticks = np.arange(0, 2.5, 0.25)
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# Adiciona grade e legenda
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()

# Salva o gráfico
plt.savefig('grafico_T_vs_sqrt_L.png')

# Imprime o resumo final
print("--- Resumo Final da Análise (Método T vs. √L) ---")
print(f"Coeficiente angular (m) da reta: {slope:.4f} s/√m")
print(f"Valor experimental de g calculado: {g_experimental:.3f} m/s²")
print(f"Valor teórico de g adotado: {g_teorico:.3f} m/s²")
print(f"Erro percentual: {erro_percentual:.2f}%")
print("\\nGráfico 'grafico_T_vs_sqrt_L.png' gerado com sucesso.")
