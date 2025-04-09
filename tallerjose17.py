import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([7.5, 5.5, 6.5, 3.5, 4.5, 3, 2.5, 1])

n = len(x)

suma_xy = np.sum(x * y)
suma_x = np.sum(x)
suma_y = np.sum(y)
suma_xcuadrado = np.sum(x**2)

a1 = (n * suma_xy - suma_x * suma_y) / (n * suma_xcuadrado - suma_x**2)

media_x = np.mean(x)
media_y = np.mean(y)

a0 = media_y - a1 * media_x

print(f"Cálculos utilizando las fórmulas exactas:")
print(f"a₁ (pendiente): {a1:.4f}")
print(f"a₀ (intercepto): {a0:.4f}")
print(f"Ecuación de la recta: y = {a0:.4f} + {a1:.4f}x")

y_pred = a1 * x + a0

plt.figure(figsize=(10, 6))
plt.scatter(x, y,color = "red" ,label='Datos originales')
plt.plot(x, y_pred,color = "black", label=f'Línea de regresión (y=mx+b): y = {a1:.4f}x + {a0:.4f}')
plt.title('Regresión Lineal por Mínimos Cuadrados')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

