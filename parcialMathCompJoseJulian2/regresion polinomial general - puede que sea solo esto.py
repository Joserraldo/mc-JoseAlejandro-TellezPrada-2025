import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

class RegresionPolinomialGeneral:
    def __init__(self, x, y, grado):
        self.x = x
        self.y = y
        self.grado = grado
        self.n = len(x)
        self.coeficientes = []
        self.y_pred = []
        self.r2 = 0
        self.r = 0
        self.sy = 0
        self.sy_x = 0

    def calcular(self):
        n = self.n
        g = self.grado
        x = self.x
        y = self.y

        sum_potencias = [sum(xi**k for xi in x) for k in range(2 * g + 1)]
        sum_xy = [sum((x[i]**k) * y[i] for i in range(n)) for k in range(g + 1)]

        A = [[sum_potencias[i + j] for j in range(g + 1)] for i in range(g + 1)]
        B = sum_xy[:]

        def resolver_sistema(A, B):
            size = len(B)
            for i in range(size):
                if A[i][i] == 0:
                    for j in range(i + 1, size):
                        if A[j][i] != 0:
                            A[i], A[j] = A[j], A[i]
                            B[i], B[j] = B[j], B[i]
                            break
                for j in range(i + 1, size):
                    factor = A[j][i] / A[i][i]
                    for k in range(i, size):
                        A[j][k] -= factor * A[i][k]
                    B[j] -= factor * B[i]
            coef = [0] * size
            for i in range(size - 1, -1, -1):
                suma = sum(A[i][j] * coef[j] for j in range(i + 1, size))
                coef[i] = (B[i] - suma) / A[i][i]
            return coef

        self.coeficientes = resolver_sistema(A, B)

        self.y_pred = [
            sum(self.coeficientes[k] * x[i]**k for k in range(g + 1))
            for i in range(n)
        ]

        y_mean = sum(y) / n
        st = sum((y[i] - y_mean)**2 for i in range(n))
        sr = sum((y[i] - self.y_pred[i])**2 for i in range(n))

        self.sy = sqrt(st / (n - 1)) if n > 1 else 0
        self.sy_x = sqrt(sr / (n - g - 1)) if n > g + 1 else 0
        self.r2 = 1 - sr / st if st != 0 else 0
        self.r = sqrt(self.r2) * 100 if self.r2 >= 0 else 0

    def graficar(self):
        coef = self.coeficientes
        g = self.grado
        a_texto = " + ".join(
            f"{coef[k]:.4f}x^{k}" if k > 0 else f"{coef[k]:.4f}" for k in range(len(coef))
        )
        a_texto = a_texto.replace("x^1", "x")

        plt.figure(figsize=(10, 6))
        plt.scatter(self.x, self.y, color="red", label="Datos originales")

        x_suave = np.linspace(min(self.x), max(self.x), 300)
        y_suave = sum(coef[k] * x_suave**k for k in range(g + 1))

        plt.plot(x_suave, y_suave, color="blue", label=f"y = {a_texto}")
        plt.title(f"Regresión Polinomial de Grado {g}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()

        texto = (
            f"Ecuación: y = {a_texto}\n"
            f"R² = {self.r2:.4f}\n"
            f"r = {self.r:.2f}%\n"
            f"sy = {self.sy:.4f}\n"
            f"sy/x = {self.sy_x:.4f}"
        )
        plt.figtext(0.5, 0.02, texto, ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.8})
        plt.tight_layout()
        plt.show()


def buscar_mejor_regresion_polinomial(x, y, r2_objetivo=0.95):
    max_grado = len(x) - 1
    for grado in range(1, max_grado + 1):
        modelo = RegresionPolinomialGeneral(x, y, grado)
        modelo.calcular()
        modelo.graficar()
        if modelo.r2 >= r2_objetivo:
            break


'''# EJEMPLO DE USO (muestra varias funciones porque las primeras no cumplen con R² >= 0.95):
x = [0, 1, 2, 3, 4, 5]
y = [1, 2.2, 3.8, 8.5, 16, 25]
buscar_mejor_regresion_polinomial(x, y)'''
