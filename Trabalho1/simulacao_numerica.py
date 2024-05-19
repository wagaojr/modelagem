import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

# Definir a função de transferência
# Exemplo: G(s) = (100/16) [(s^2 + 16)/(s^2 + 0.2s + 100)]
numerator = [100, 0, 1600]  # Numerador
denominator = [16, 3.2, 1600]  # Denominador

# Criar a função de transferência
system = ctrl.TransferFunction(numerator, denominator)

# Gerar o diagrama de Bode
mag, phase, omega = ctrl.bode(system, dB=True, Hz=False, deg=True, plot=True)

# Exibir os gráficos
#plt.show() # gráfico do bode

time = np.linspace(0, 10, 1000)

frequencia = 100
cos_input = np.cos(frequencia * time)

time, resposta = ctrl.forced_response(system, T=time, U=cos_input)

plt.figure()
plt.plot(time, cos_input, label='Entrada de Cosseno')
plt.plot(time, resposta, label='Resposta do Sistema')
plt.title('Resposta à Entrada de Cosseno')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()


