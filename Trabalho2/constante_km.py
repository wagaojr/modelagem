import numpy as np
from scipy.optimize import curve_fit

# Dados de exemplo (x, y)
x = np.array([16, 35, 54, 73, 91, 111, 130, 150, 169, 188])
ia = np.array([1,1,1,1,1,1,1,2,2,2])
y = np.array([1, 2, 3, 4, 4.9, 5.9, 6.9, 7.9, 8.9, 9.9])

# Defina a função de ajuste (equação) que você deseja
# Por exemplo, uma função linear f(x) = m*x + c
def linear_equation(x, m, c):
    return x * m 

# Calcula os coeficientes de ajuste (m, c) usando curve_fit
params, _ = curve_fit(linear_equation, x, y)

# Extraia a inclinação (m) dos parâmetros ajustados
m = params[0]

# Exibe a inclinação da regressão linear
print(f"Inclinação (m): {m}")
