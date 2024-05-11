import matplotlib.pyplot as plt
import numpy as np

# Dados fictícios
dias = np.arange(1, 31)
elevacao = np.random.uniform(low=20, high=40, size=30)

plt.figure(figsize=(10, 6))
plt.plot(dias, elevacao, marker='o', linestyle='-', color='b')
plt.title('Elevação do Rio ao Longo do Mês')
plt.xlabel('Dia do Mês')
plt.ylabel('Elevação (m)')
plt.grid(True)
# Salva o gráfico na pasta static/images
plt.savefig('static/img/grafico_elevacao.png')
