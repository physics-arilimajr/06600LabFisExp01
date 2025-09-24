import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados do experimento
data = {
    'L (Comp. do Fio) Metros': [1.00, 0.90, 0.80, 0.70, 0.60, 0.50, 0.40, 0.30, 0.20, 0.10],
    'T(Período) Segundos': [2.04, 1.92, 1.80, 1.66, 1.54, 1.47, 1.34, 1.11, 0.96, 0.70]
}
df = pd.DataFrame(data)

# --- Geração do Gráfico T vs L ---
plt.figure(figsize=(10, 7))

# Plota os dados experimentais como um gráfico de dispersão (pontos)
plt.scatter(df['L (Comp. do Fio) Metros'], df['T(Período) Segundos'], color='blue', zorder=5, label='Dados Experimentais (L, T)')

# Adiciona a curva teórica para comparação, usando o g experimental
g_experimental = 9.941
L_curve = np.linspace(0.1, 1.0, 100) # Gera 100 pontos para uma curva suave
T_curve = 2 * np.pi * np.sqrt(L_curve / g_experimental)
plt.plot(L_curve, T_curve, color='red', linestyle='--', label=f'Curva Teórica (g={g_experimental:.3f} m/s²)')

# Define o título e os rótulos dos eixos
plt.title('Período do Pêndulo vs. Comprimento do Fio', fontsize=16)
plt.xlabel('L (Comprimento do Fio) em metros', fontsize=12)
plt.ylabel('T (Período) em segundos', fontsize=12)

# Define as marcações (ticks) específicas para os eixos, conforme solicitado
x_ticks = np.arange(0, 1.1, 0.1)
y_ticks = np.arange(0, 2.5, 0.25)
plt.xticks(x_ticks)
plt.yticks(y_ticks)

# Define os limites dos eixos para um bom enquadramento
plt.xlim(0, 1.05)
plt.ylim(0, 2.3)

# Adiciona uma grade para facilitar a leitura
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Adiciona a legenda
plt.legend()

# Salva o gráfico em um arquivo
plt.savefig('grafico_T_vs_L.png')

print("Gráfico 'grafico_T_vs_L.png' gerado com sucesso.")
