import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

x = np.array([ 1, 2, 3, 4, 5, 6,7])
y = np.array([ 0.5, 2.5, 2, 4, 3.5, 6,5.5])
n = len(x)

media_x = np.mean(x)
media_y = np.mean(y)

suma_xy = np.sum(x * y)
suma_x = np.sum(x)
suma_y = np.sum(y)
suma_x_cuadrado = np.sum(x**2)
suma_y_cuadrado = np.sum(y**2)

a1 = (n * suma_xy - suma_x * suma_y) / (n * suma_x_cuadrado - suma_x**2)
a0 = media_y - a1 * media_x

y_pred = a1 * x + a0
st = np.sum((y - media_y)**2)
sr = np.sum((y - y_pred)**2)

sy = np.sqrt(st / (n - 1))
sy_x = np.sqrt(sr / (n - 2))

r_cuadrado = 1 - (sr / st)

r = sqrt(r_cuadrado)*100

plt.figure(figsize=(12, 8))

plt.scatter(x, y, color="red", label='Datos originales')
plt.plot(x, y_pred, color="blue", label=f'Línea de regresión: y = {a0:.4f} + {a1 :.4f}x')

resultados = f"""
Desviación estándar (sy): {sy:.4f}
Error estándar de la estimación (sy/x): {sy_x:.4f}
Coeficiente de determinación (r²): {r_cuadrado:.4f}
Coeficiente de correlación (r): {r:.4f}%
Ecuación de regresión: y = {a0:.4f} + {a1:.4f}x
"""
plt.figtext(0.5, 0.03, resultados, ha='center', fontsize=12, bbox={"facecolor":"grey", "alpha":0.8, "pad":5})
plt.title('Análisis de Regresión Lineal')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()
plt.subplots_adjust(bottom=0.3) 
plt.show()