import numpy as np
import matplotlib.pyplot as plt
import cmath

e = cmath.exp
k1 = -525
k2 = -1.25

# Defina a função que você deseja plotar
def y(t):
    return k1*((-e(-t/10)*cmath.sin(3*cmath.sqrt(1111)*t/10))/(300*cmath.sqrt(1111)) - (-e(-t/10)*cmath.cos(3*cmath.sqrt(1111)*t/10))/(100) + (1/100)) + k2*((10*e(-t/10)*cmath.sin(3*cmath.sqrt(1111)*t/10))/(3*cmath.sqrt(1111))) + 6.25

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
plt.title('y(t) para cos(t)')
plt.legend()
plt.grid(True)

plt.show()