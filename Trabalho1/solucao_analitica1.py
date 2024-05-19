import numpy as np
import matplotlib.pyplot as plt
import cmath

e = cmath.exp
i = 1j
# Defina a função que você deseja plotar
def y(t):
    return (100/16)*((0.42424 + 0.00577269*i)*e((-0.1 - 9.9995*i)*t)*((0.99963 - 0.0272092*i) + (1 + 0*i)*e((19.999*i)*t)) + ((0.075755 - 0.00015*i)*e(-i*t)*((0.999992 + 0.00396012*i) + (1 + 0*i)*e((2*i)*t))))

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
plt.xlabel('Tempo (t)')
plt.ylabel('y(t)')
plt.title('Gráfico da função y(t)')
plt.legend()
plt.grid(True)

plt.show()
