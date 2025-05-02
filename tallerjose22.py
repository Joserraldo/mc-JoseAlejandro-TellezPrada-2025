import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x1 = np.array([1, 1, 2, 3, -1.5, 2, 3, 3])
x2 = np.array([0, 0.5, 0.5, 1, -1.2, 1.5, 1.5, 0.5])
y = np.array([0.2, 3, -0.8, -0.4, 3.5, 3.6, 0.5, -1])


def calcular_coeficientes_regresion_multiple(x1, x2, y):
    
    n = len(x1)
    
    
    sum_x1 = np.sum(x1)
    sum_x2 = np.sum(x2)
    sum_y = np.sum(y)
    
    sum_x1_squared = np.sum(x1**2)
    sum_x2_squared = np.sum(x2**2)
    
    sum_x1_x2 = np.sum(x1 * x2)
    
    sum_x1_y = np.sum(x1 * y)
    sum_x2_y = np.sum(x2 * y)
    
    
    A = np.array([
        [n, sum_x1, sum_x2],
        [sum_x1, sum_x1_squared, sum_x1_x2],
        [sum_x2, sum_x1_x2, sum_x2_squared]
    ])
    
    B = np.array([sum_y, sum_x1_y, sum_x2_y])
    
    
    coeficientes = np.linalg.solve(A, B)
    
    return coeficientes


coeficientes = calcular_coeficientes_regresion_multiple(x1, x2, y)
a0, a1, a2 = coeficientes

print(f"Ecuación del plano: y = {a0:.6f} + {a1:.6f}x₁ + {a2:.6f}x₂")


def funcion_lineal(x1, x2, coef):
    return coef[0] + coef[1] * x1 + coef[2] * x2


y_estimado = funcion_lineal(x1, x2, coeficientes)


y_mean = np.mean(y)
ss_total = np.sum((y - y_mean)**2)  
ss_residual = np.sum((y - y_estimado)**2)  
r2 = 1 - (ss_residual / ss_total)
print(f"Coeficiente de determinación (R²): {r2:.6f}")


r = np.sqrt(np.abs(r2))
print(f"Coeficiente de correlación (r): {r:.6f}")


Sr = np.sum((y - y_estimado)**2)
print(f"Suma de los cuadrados de los residuos (Sr): {Sr:.6f}")


fig = plt.figure(figsize=(16, 10))


ax = fig.add_subplot(121, projection='3d')


ax.scatter(x1, x2, y, color='blue', marker='o', label='Datos originales')


x1_range = np.linspace(min(x1)-0.5, max(x1)+0.5, 20)
x2_range = np.linspace(min(x2)-0.5, max(x2)+0.5, 20)
X1, X2 = np.meshgrid(x1_range, x2_range)
Y = funcion_lineal(X1, X2, coeficientes)


surface = ax.plot_surface(X1, X2, Y, color='red', alpha=0.5, label='Plano de regresión')


surface._facecolors2d = surface._facecolor3d
surface._edgecolors2d = surface._edgecolor3d


ax.set_title('Regresión Lineal Múltiple (Dos Dimensiones)')
ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('y')


info_text = (
    f'Ecuación: y = {a0:.4f} + {a1:.4f}x₁ + {a2:.4f}x₂\n'
    f'R² = {r2:.4f}\n'
    f'r = {r:.4f}\n'
    f'Suma de residuos² = {Sr:.4f}'
)
ax.text2D(0.5, 0.05, info_text, transform=ax.transAxes, 
          bbox=dict(facecolor='white', alpha=0.8))


ax2 = fig.add_subplot(122)
ax2.scatter(y, y_estimado, color='blue')
ax2.plot([min(y), max(y)], [min(y), max(y)], 'r--')  
ax2.set_xlabel('Valores reales (y)')
ax2.set_ylabel('Valores predichos (ŷ)')
ax2.set_title('Valores Reales vs. Predichos')
ax2.grid(True)


tabla_comp = 'x₁     x₂      y real    y pred    Residuo\n'
tabla_comp += '----------------------------------------\n'
for i in range(len(y)):
    tabla_comp += f'{x1[i]:<6.1f} {x2[i]:<6.1f} {y[i]:<9.2f} {y_estimado[i]:<9.2f} {y[i]-y_estimado[i]:<9.2f}\n'

ax2.text(1.05, 0.5, tabla_comp, transform=ax2.transAxes, fontfamily='monospace', 
         bbox=dict(facecolor='white', alpha=0.8), va='center')

plt.savefig('regresion_lineal_multiple.png', bbox_inches='tight')
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(range(len(y)), y - y_estimado, color='green')
plt.axhline(y=0, color='red', linestyle='-')
plt.title('Residuos de la Regresión')
plt.xlabel('Índice de la muestra')
plt.ylabel('Residuo')
plt.grid(True)
