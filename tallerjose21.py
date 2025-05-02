import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 2, 4, 6, 8, 10, 12])
y = np.array([7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2])

def calcular_coeficientes_polinomio(x, y):
    
    n = len(x)    
    
    sum_x = np.sum(x)
    sum_x2 = np.sum(x**2)
    sum_x3 = np.sum(x**3)
    sum_x4 = np.sum(x**4)
    
    sum_y = np.sum(y)
    sum_xy = np.sum(x*y)
    sum_x2y = np.sum((x**2)*y)
      
    A = np.array([
        [n, sum_x, sum_x2],
        [sum_x, sum_x2, sum_x3],
        [sum_x2, sum_x3, sum_x4]
    ])
    
    B = np.array([sum_y, sum_xy, sum_x2y])
    
    
    coeficientes = np.linalg.solve(A, B)
    
    return coeficientes

coeficientes = calcular_coeficientes_polinomio(x, y)
a0, a1, a2 = coeficientes

print(f"Ecuación del polinomio: y = {a0:.6f} + {a1:.6f}x + {a2:.6f}x²")

def polinomio(x, coef):
    return coef[0] + coef[1] * x + coef[2] * x**2

y_estimado = polinomio(x, coeficientes)

y_mean = np.mean(y)
ss_total = np.sum((y - y_mean)**2)  
ss_residual = np.sum((y - y_estimado)**2)  
r2 = 1 - (ss_residual / ss_total)
print(f"Coeficiente de determinación (R²): {r2:.6f}")

r = np.sqrt(np.abs(r2))  
print(f"Coeficiente de correlación (r): {r:.6f}")

Sr = np.sum((y - y_estimado)**2)
print(f"Suma de los cuadrados de los residuos (Sr): {Sr:.6f}")

plt.figure(figsize=(10, 6))

plt.scatter(x, y, color='blue', label='Datos originales')

x_curve = np.linspace(min(x), max(x), 100)
y_curve = polinomio(x_curve, coeficientes)

plt.plot(x_curve, y_curve, color='red', label=f'Polinomio: {a0:.2f} + {a1:.2f}x + {a2:.2f}x²')

plt.title('Regresión Polinomial de Segundo Grado')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

plt.savefig('regresion_polinomial.png')
plt.show()