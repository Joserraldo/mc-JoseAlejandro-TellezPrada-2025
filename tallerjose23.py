import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, expand

def lagrange_basis(x_values, i, x):

    n = len(x_values)
    result = 1.0
    for j in range(n):
        if j != i:
            result *= (x - x_values[j]) / (x_values[i] - x_values[j])
    return result

def lagrange_interpolation(x_values, y_values, x, degree=None):

    if degree is None:
        degree = len(x_values) - 1
    else:
        degree = min(degree, len(x_values) - 1)
    
    result = 0.0
    for i in range(degree + 1):
        result += y_values[i] * lagrange_basis(x_values[:degree+1], i, x)
    return result

def lagrange_polynomial_symbolic(x_values, y_values, degree=None):

    if degree is None:
        degree = len(x_values) - 1
    else:
        degree = min(degree, len(x_values) - 1)
    
    x = symbols('x')
    polynomial = 0
    
    for i in range(degree + 1):
        term = y_values[i]
        for j in range(degree + 1):
            if j != i:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        polynomial += term
    
    return expand(polynomial)


x_values = [1, 3, 5, 7, 9]
y_values = [3, 0, -1, 2.5, 1]
x_punto = 4.25


poly_grado1 = lagrange_polynomial_symbolic(x_values, y_values, 1)
poly_grado2 = lagrange_polynomial_symbolic(x_values, y_values, 2)


estimate_grado1 = lagrange_interpolation(x_values, y_values, x_punto, 1)
estimate_grado2 = lagrange_interpolation(x_values, y_values, x_punto, 2)
estimate_grado3 = lagrange_interpolation(x_values, y_values, x_punto, 3)



plt.figure(figsize=(10, 6))


plt.scatter(x_values, y_values, color='red', label='Puntos base')


x_curve = np.linspace(min(x_values), max(x_values), 100)


y_curve1 = [lagrange_interpolation(x_values, y_values, x, 1) for x in x_curve]
y_curve2 = [lagrange_interpolation(x_values, y_values, x, 2) for x in x_curve]
y_curve3 = [lagrange_interpolation(x_values, y_values, x, 3) for x in x_curve]
plt.plot(x_curve, y_curve1, label='Grado 1')
plt.plot(x_curve, y_curve2, label='Grado 2')
plt.plot(x_curve, y_curve3, label='Grado 3')


plt.scatter([x_punto], [estimate_grado1], color='green', s=80, label=f'f({x_punto}) grado 1 : {estimate_grado1}')
plt.scatter([x_punto], [estimate_grado2], color='blue', s=80, label=f'f({x_punto}) grado 2: {estimate_grado2}')
plt.scatter([x_punto], [estimate_grado3], color='purple', s=80, label=f'f({x_punto}) grado 3: {estimate_grado3}')


plt.axvline(x=x_punto, color='gray', linestyle='--', alpha=0.5)



plt.grid(True)
plt.legend()
plt.title('Polinomios de Interpolación de Lagrange')
plt.xlabel('x')
plt.ylabel('f(x)')

plt.show()



x_detallado = [3, 5]
y_detallado = [0, -1]

L0 = (x_punto - x_detallado[1]) / (x_detallado[0] - x_detallado[1])
L1 = (x_punto - x_detallado[0]) / (x_detallado[1] - x_detallado[0])


x_detallado = [3, 5, 7]
y_detallado = [0, -1, 2.5]

L0 = ((x_punto - x_detallado[1]) * (x_punto - x_detallado[2])) / ((x_detallado[0] - x_detallado[1]) * (x_detallado[0] - x_detallado[2]))
L1 = ((x_punto - x_detallado[0]) * (x_punto - x_detallado[2])) / ((x_detallado[1] - x_detallado[0]) * (x_detallado[1] - x_detallado[2]))
L2 = ((x_punto - x_detallado[0]) * (x_punto - x_detallado[1])) / ((x_detallado[2] - x_detallado[0]) * (x_detallado[2] - x_detallado[1]))
