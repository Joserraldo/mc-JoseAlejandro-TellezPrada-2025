import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

class RegresionPolinomialGrado2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.coeficientes = [0, 0, 0]  
        self.y_pred = []
        self.r2 = 0
        self.r = 0
        self.sy = 0
        self.sy_x = 0

    def calcular(self):
        n = self.n
        x = self.x
        y = self.y

        sum_x = sum(x)
        sum_x2 = sum(xi**2 for xi in x)
        sum_x3 = sum(xi**3 for xi in x)
        sum_x4 = sum(xi**4 for xi in x)

        sum_y = sum(y)
        sum_xy = sum(x[i]*y[i] for i in range(n))
        sum_x2y = sum((x[i]**2)*y[i] for i in range(n))

        A = [
            [n,     sum_x,  sum_x2],
            [sum_x, sum_x2, sum_x3],
            [sum_x2, sum_x3, sum_x4]
        ]
        B = [sum_y, sum_xy, sum_x2y]

        def resolver_sistema_3x3(A, B):
            for i in range(1, 3):
                factor = A[i][0] / A[0][0]
                for j in range(3):
                    A[i][j] -= factor * A[0][j]
                B[i] -= factor * B[0]

            factor = A[2][1] / A[1][1]
            for j in range(1, 3):
                A[2][j] -= factor * A[1][j]
            B[2] -= factor * B[1]

            a2 = B[2] / A[2][2]
            a1 = (B[1] - A[1][2]*a2) / A[1][1]
            a0 = (B[0] - A[0][1]*a1 - A[0][2]*a2) / A[0][0]
            return [a0, a1, a2]

        self.coeficientes = resolver_sistema_3x3(A, B)
        a0, a1, a2 = self.coeficientes

        self.y_pred = [a0 + a1 * xi + a2 * xi**2 for xi in x]

        y_mean = sum(y) / n
        st = sum((yi - y_mean)**2 for yi in y)
        sr = sum((y[i] - self.y_pred[i])**2 for i in range(n))

        self.sy = sqrt(st / (n - 1)) if n > 1 else 0
        self.sy_x = sqrt(sr / (n - 3)) if n > 3 else 0
        self.r2 = 1 - sr / st if st != 0 else 0
        self.r = sqrt(self.r2) * 100 if self.r2 >= 0 else 0

    def graficar(self):
        a0, a1, a2 = self.coeficientes
        plt.figure(figsize=(10, 6))
        plt.scatter(self.x, self.y, color="red", label="Datos originales")

        x_suave = np.linspace(min(self.x), max(self.x), 200)
        y_suave = a0 + a1 * x_suave + a2 * x_suave ** 2

        plt.plot(x_suave, y_suave, color="blue", label=f"y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x²")
        plt.title("Regresión Polinomial de Segundo Grado")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()

        texto = (
            f"Ecuación: y = {a0:.4f} + {a1:.4f}x + {a2:.4f}x²\n"
            f"R² = {self.r2:.4f}\n"
            f"r = {self.r:.2f}%\n"
            f"sy = {self.sy:.4f}\n"
            f"sy/x = {self.sy_x:.4f}"
        )
        plt.figtext(0.5, 0.02, texto, ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.8})
        plt.tight_layout()
        plt.show()

'''# EJEMPLO DE USO (puedes comentar esto cuando lo integres al código general):
x = [0, 2, 4, 6, 8, 10, 12]
y = [7.5, 1.8, -1, -1.8, -1.2, 2.2, 7.2]
modelo = RegresionPolinomialGrado2(x, y)
modelo.calcular()
modelo.graficar()'''
