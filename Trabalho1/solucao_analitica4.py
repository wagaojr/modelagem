import numpy as np
import matplotlib.pyplot as plt
import cmath

e = cmath.exp
i = 1j
# Defina a função que você deseja plotar
def y(t):
    return (100/16)*()

# Defina o intervalo de tempo
t_min = 0
t_max = 10
num_points = 1000  # Número de pontos no gráfico

# Crie um vetor de tempo de t_min a t_max
t = np.linspace(t_min, t_max, num_points)

# Calcule os valores da função f(t) para cada ponto de tempo
y = np.array([y(t) for t in t])

# Crie o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='y(t)', color='b')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('y(t) para cos(100t)')
plt.legend()
plt.grid(True)

plt.show()