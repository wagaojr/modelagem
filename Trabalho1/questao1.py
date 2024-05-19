import matplotlib.pyplot as plt
import control as ctrl

# Definir a função de transferência
# Exemplo: G(s) = (100/16) [(s^2 + 16)/(s^2 + 0.2s + 100)]
numerator = [100, 0, 1600]  # Numerador
denominator = [16, 3.2, 1600]  # Denominador

# Criar a função de transferência
system = ctrl.TransferFunction(numerator, denominator)

# Gerar o diagrama de Bode
mag, phase, omega = ctrl.bode(system, dB=True, Hz=False, deg=True, plot=True)

# Exibir os gráficos
plt.show()
