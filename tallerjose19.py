import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

x = np.array([ 1, 2, 3, 4, 5,6])
y = np.array([ 1.5, 2.5, 3.5, 4.5, 6.5, 9]) 
ln_y = np.log(y)
n = len(x)

media_x = np.mean(x)
media_y = np.mean(ln_y)

suma_xy = np.sum(x * ln_y)
suma_x = np.sum(x)
suma_y = np.sum(ln_y)
suma_x_cuadrado = np.sum(x**2)
suma_y_cuadrado = np.sum(ln_y**2)

a1 = (n * suma_xy - suma_x * suma_y) / (n * suma_x_cuadrado - suma_x**2)
a0 = media_y - a1 * media_x

beta = a1  
alpha = exp(a0)  

y_pred_ln = a1 * x + a0  
y_pred = alpha * np.exp(beta * x)  

st = np.sum((ln_y - media_y)**2)
sr = np.sum((ln_y - y_pred_ln)**2)

sy = np.sqrt(st / (n - 1))
sy_x = np.sqrt(sr / (n - 2))

r_cuadrado = 1 - (sr / st)
r = sqrt(r_cuadrado) * 100

plt.figure(figsize=(12, 8))

plt.scatter(x, y, color="red", label='Datos originales')
plt.plot(x, y_pred, color="blue", label=f'Línea de regresión: y = {alpha:.4f}e^{beta:.4f}x')

resultados = f"""
Desviación estándar (sy): {sy:.4f}
Error estándar de la estimación (sy/x): {sy_x:.4f}
Coeficiente de determinación (r²): {r_cuadrado:.4f}
Coeficiente de correlación (r): {r:.4f}%
Ecuación de regresión: y = {alpha:.4f}e^{beta:.4f}x
"""
plt.figtext(0.5, 0.03, resultados, ha='center', fontsize=12, bbox={"facecolor":"grey", "alpha":0.8, "pad":5})
plt.title('Análisis de Regresión Exponencial')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.subplots_adjust(bottom=0.3) 
plt.show()
