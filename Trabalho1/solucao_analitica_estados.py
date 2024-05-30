import numpy as np
import matplotlib.pyplot as plt
import cmath

e = cmath.exp
k1 = -525
k2 = -1.25

# Defina a função que você deseja plotar
def y(t):
    return (525*e(-t/10)*cmath.sin(10*t))/10000 - (525*e(-t/10)*cmath.cos(10*t))/100 - (12.5*e(-t/10)*cmath.sin(10*t))/100 + 1
# Defina o intervalo de tempo
t_min = 0
t_max = 60
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
plt.title('y(t) para degrau na equação de estados')
plt.legend()
plt.grid(True)

plt.show()