import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados do experimento
data = {
    'L (Comp. do Fio) Metros': [1.00, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10],
    'T(Período) Segundos': [2.04, 1.92, 1.80, 1.66, 1.54, 1.47, 1.34, 1.11, 0.96, 0.70]
}
df = pd.DataFrame(data)

# Etapa 1: Calcular o quadrado do período
df['T^2'] = df['T(Período) Segundos']**2

# Etapa 2: Realizar a regressão linear
slope, intercept = np.polyfit(df['L (Comp. do Fio) Metros'], df['T^2'], 1)

# Cria os pontos para a reta de ajuste
x_line = np.array([0, 1.0])
y_line = slope * x_line + intercept

# Etapa 3: Geração do Gráfico
plt.figure(figsize=(10, 7))
plt.scatter(df['L (Comp. do Fio) Metros'], df['T^2'], color='blue', zorder=5, label='Dados Experimentais ($L, T^2$)')
plt.plot(x_line, y_line, color='red', label=f'Ajuste Linear (y={slope:.2f}x + {intercept:.2f})')
plt.title('Análise do Pêndulo: Período ao Quadrado vs. Comprimento do Fio', fontsize=16)
plt.xlabel('L (Comprimento do Fio) em metros', fontsize=12)
plt.ylabel('$T^2$ (Período ao Quadrado) em $s^2$', fontsize=12)
x_ticks = np.arange(0, 1.1, 0.1)
y_ticks = np.arange(0, 5.0, 0.5)
plt.xticks(x_ticks)
plt.yticks(y_ticks)
plt.xlim(0, 1.05)
plt.ylim(0, 4.55)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('grafico_pendulo_final_linear.png')

# Etapa 4: Calcular o valor experimental da gravidade
g_experimental = 4 * (np.pi**2) / slope

# Etapa 5: Comparar com o valor teórico e calcular o erro
g_teorico = 9.807  # m/s²
erro_percentual = (abs(g_experimental - g_teorico) / g_teorico) * 100

# Impressão dos Resultados
print("--- Análise Experimental da Gravidade (g) ---")
print(f"Coeficiente angular (m) da reta: {slope:.4f} s²/m")
print(f"Valor experimental de g calculado: {g_experimental:.3f} m/s²")
print(f"Valor teórico de g adotado: {g_teorico:.3f} m/s²")
print(f"Erro percentual: {erro_percentual:.2f}%")
print("\nGráfico 'grafico_pendulo_final_linear.png' gerado com sucesso.")
