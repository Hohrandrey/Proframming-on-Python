import numpy as np
import matplotlib.pyplot as plt


mu = np.linspace(0.0, 4.0, 40)
x = 0.1 * np.ones_like(mu)

# Настройка графика
plt.figure(figsize=(12, 7), facecolor='white')

for _ in range(100):
    x = mu * x * (1 - x)
    if _ >= 50:
        plt.scatter(mu, x, color='black', s=40, alpha=0.9, edgecolors='none')

plt.title("Диаграмма бифуркаций", fontsize=16, pad=20)
plt.xlabel("μ", fontsize=14)
plt.ylabel("x", fontsize=14)
plt.grid(alpha=0.1)
plt.tight_layout()
plt.show()