import numpy as np
import matplotlib.pyplot as plt

x = np.array([0.063, 0.132, 0.220, 0.277, 0.383, 0.471, 0.605, 0.674, 0.716, 0.937])
y = np.array([1, 2, 3, 4, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9])

# Calcula os coeficientes da regressão linear (intercepto e inclinação)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]

regression_line = m * x + c

plt.scatter(x, y, color='blue', label='Dados')
plt.plot(x, regression_line, color='red', label='Linha de Regressão')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regressão Linear')
plt.legend()
plt.show()

print(f"Inclinação (m): {m}")
print(f"Intercepto (c): {c}")
