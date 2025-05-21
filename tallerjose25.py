import copy
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

# Gauss-Jordan
def gaussJordan(a, b):
    a = copy.deepcopy(a)
    b = b.copy()
    n = len(b)

    for i in range(n):
        if a[i][i] == 0:
            for k in range(i + 1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    break

        div = a[i][i]
        a[i] = [val / div for val in a[i]]
        b[i] /= div

        for j in range(n):
            if j != i:
                factor = a[j][i]
                a[j] = [a[j][k] - factor * a[i][k] for k in range(n)]
                b[j] -= factor * b[i]

    return b

# Trazadores cúbicos
def trazadoresCubicos(x, y):
    n = len(x)
    h = [x[i+1] - x[i] for i in range(n-1)]

    A = [[0.0 for _ in range(n-2)] for _ in range(n-2)]
    b = [0.0 for _ in range(n-2)]

    for i in range(1, n-1):
        A[i-1][i-1] = 2 * (h[i-1] + h[i])
        if i > 1:
            A[i-1][i-2] = h[i-1]
        if i < n-2:
            A[i-1][i] = h[i]
        b[i-1] = 6 * ((y[i+1] - y[i])/h[i] - (y[i] - y[i-1])/h[i-1])

    M = [0.0] + gaussJordan(A, b) + [0.0]

    coeficientes = []
    for i in range(n - 1):
        hi = h[i]
        Ai = (M[i+1] - M[i]) / (6 * hi)
        Bi = M[i] / 2
        Ci = (y[i+1] - y[i]) / hi - (hi / 6) * (M[i+1] + 2 * M[i])
        Di = y[i]
        coeficientes.append([Ai, Bi, Ci, Di, x[i]])

    return coeficientes

def evaluar_trazador(coeficientes, x_valor):
    for coef in coeficientes:
        a, b, c, d, xi = coef
        next_index = coeficientes.index(coef) + 1
        if next_index == len(coeficientes) or x_valor < coeficientes[next_index][4]:
            dx = x_valor - xi
            return a * dx**3 + b * dx**2 + c * dx + d
    return None

# Lagrange
def multiplicar_polinomio(p1, p2):
    grado = len(p1) + len(p2) - 2
    resultado = [Fraction(0)] * (grado + 1)
    for i, a in enumerate(p1):
        for j, b in enumerate(p2):
            resultado[i + j] += a * b
    return resultado

def sumar_polinomios(p1, p2):
    longitud = max(len(p1), len(p2))
    resultado = [Fraction(0)] * longitud
    for i in range(len(p1)):
        resultado[i] += p1[i]
    for i in range(len(p2)):
        resultado[i] += p2[i]
    return resultado

def evaluar_polinomio(coeficientes, x_valor):
    resultado = 0
    for coef in coeficientes:
        resultado = resultado * x_valor + coef
    return resultado

# Función principal combinada
def main():
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 5, 2.5, 4, -1.6, 2]
    punto_a_estimar = 3.55

    # LAGRANGE
    x_frac = [Fraction(i) for i in x]
    y_frac = [Fraction(i) for i in y]
    n = len(x)
    polinomio_final = [Fraction(0)]

    for i in range(n):
        numerador = [Fraction(1)]
        denominador = Fraction(1)
        for j in range(n):
            if i != j:
                numerador = multiplicar_polinomio(numerador, [-x_frac[j], 1])
                denominador *= (x_frac[i] - x_frac[j])
        li = [(coef * y_frac[i]) / denominador for coef in numerador]
        polinomio_final = sumar_polinomios(polinomio_final, li)

    coefs_float = [float(c) for c in reversed(polinomio_final)]
    valor_lagrange = evaluar_polinomio(coefs_float, punto_a_estimar)

    # TRAZADORES 
    coeficientes_cubicos = trazadoresCubicos(x, y)
    valor_trazador = evaluar_trazador(coeficientes_cubicos, punto_a_estimar)

    # GRÁFICA 
    xs = np.linspace(min(x) - 0.5, max(x) + 0.5, 500)
    ys_lagrange = np.polyval(coefs_float, xs)
    ys_trazador = [evaluar_trazador(coeficientes_cubicos, xi) for xi in xs]

    plt.figure(figsize=(12, 6))
    plt.plot(xs, ys_lagrange, label="Lagrange", color='blue')
    plt.plot(xs, ys_trazador, label="Trazadores Cúbicos", color='red')
    plt.scatter(x, y, color='black', zorder=5, label="Puntos dados")
    plt.axvline(punto_a_estimar, color='gray', linestyle='--', alpha=0.5)
    plt.scatter([punto_a_estimar], [valor_lagrange], color='blue', label=f"Lagrange f({punto_a_estimar}) ≈ {valor_lagrange:.4f}")
    plt.scatter([punto_a_estimar], [valor_trazador], color='red', label=f"Trazadores f({punto_a_estimar}) ≈ {valor_trazador:.4f}")

    plt.title("Comparación: Interpolación de Lagrange vs Trazadores Cúbicos")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
