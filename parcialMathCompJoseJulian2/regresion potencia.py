import matplotlib.pyplot as plt
from math import log, exp, sqrt
import numpy as np

class RegresionPotencia:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.a = 0
        self.b = 0
        self.r2 = 0
        self.r = 0
        self.sy = 0
        self.sy_x = 0
        self.y_pred = []

    def calcular(self):
        n = self.n
        x = self.x
        y = self.y

        ln_x = [log(xi) for xi in x]
        ln_y = [log(yi) for yi in y]

        suma_ln_x = sum(ln_x)
        suma_ln_y = sum(ln_y)
        suma_ln_x_ln_y = sum(ln_x[i] * ln_y[i] for i in range(n))
        suma_ln_x2 = sum(ln_x[i] ** 2 for i in range(n))

        media_ln_x = suma_ln_x / n
        media_ln_y = suma_ln_y / n

        self.b = (n * suma_ln_x_ln_y - suma_ln_x * suma_ln_y) / (n * suma_ln_x2 - suma_ln_x ** 2)
        ln_a = media_ln_y - self.b * media_ln_x
        self.a = exp(ln_a)

        self.y_pred = [self.a * (xi ** self.b) for xi in x]
        ln_y_pred = [ln_a + self.b * ln_x[i] for i in range(n)]

        st = sum((ln_y[i] - media_ln_y) ** 2 for i in range(n))
        sr = sum((ln_y[i] - ln_y_pred[i]) ** 2 for i in range(n))

        self.sy = sqrt(st / (n - 1)) if n > 1 else 0
        self.sy_x = sqrt(sr / (n - 2)) if n > 2 else 0
        self.r2 = 1 - sr / st if st != 0 else 0
        self.r = sqrt(self.r2) * 100 if self.r2 >= 0 else 0

    def graficar(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.x, self.y, color="red", label="Datos originales")

        x_suave = np.linspace(min(self.x), max(self.x), 200)
        y_suave = self.a * x_suave ** self.b

        plt.plot(x_suave, y_suave, color="blue", label=f"y = {self.a:.4f}x^{self.b:.4f}")
        plt.title("Regresión de Potencia")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()

        texto = (
            f"Ecuación: y = {self.a:.4f}x^{self.b:.4f}\n"
            f"R² = {self.r2:.4f}\n"
            f"r = {self.r:.2f}%\n"
            f"sy = {self.sy:.4f}\n"
            f"sy/x = {self.sy_x:.4f}"
        )
        plt.figtext(0.5, 0.02, texto, ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.8})
        plt.tight_layout()
        plt.show()

'''# EJEMPLO DE USO (puedes comentar esto cuando lo integres al código general):
x = [1, 2, 3, 4, 5]
y = [2.1, 4.5, 7.8, 12.3, 18.5]
modelo = RegresionPotencia(x, y)
modelo.calcular()
modelo.graficar()'''
