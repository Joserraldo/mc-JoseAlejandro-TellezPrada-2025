import matplotlib.pyplot as plt
from math import sqrt

class RegresionLineal:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.a0 = 0
        self.a1 = 0
        self.r2 = 0
        self.r = 0
        self.sy = 0
        self.sy_x = 0
        self.y_pred = []

    def calcular(self):
        n = self.n
        x = self.x
        y = self.y

        suma_x = sum(x)
        suma_y = sum(y)
        suma_xy = sum(x[i] * y[i] for i in range(n))
        suma_x2 = sum(x[i] ** 2 for i in range(n))

        media_x = suma_x / n
        media_y = suma_y / n

        self.a1 = (n * suma_xy - suma_x * suma_y) / (n * suma_x2 - suma_x ** 2)
        self.a0 = media_y - self.a1 * media_x

        self.y_pred = [self.a0 + self.a1 * xi for xi in x]

        st = sum((y[i] - media_y) ** 2 for i in range(n))
        sr = sum((y[i] - self.y_pred[i]) ** 2 for i in range(n))

        self.sy = sqrt(st / (n - 1)) if n > 1 else 0
        self.sy_x = sqrt(sr / (n - 2)) if n > 2 else 0
        self.r2 = 1 - sr / st if st != 0 else 0
        self.r = sqrt(self.r2) * 100 if self.r2 >= 0 else 0


    def graficar(self):
        plt.figure(figsize=(10, 6))
        plt.scatter(self.x, self.y, color="red", label="Datos originales")
        plt.plot(self.x, self.y_pred, color="blue", label=f"y = {self.a0:.4f} + {self.a1:.4f}x")
        plt.title("Regresión Lineal")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()

        texto = (
            f"Ecuación: y = {self.a0:.4f} + {self.a1:.4f}x\n"
            f"R² = {self.r2:.4f}\n"
            f"r = {self.r:.2f}%\n"
            f"sy = {self.sy:.4f}\n"
            f"sy/x = {self.sy_x:.4f}"
        )
        plt.figtext(0.5, 0.02, texto, ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.8})
        plt.tight_layout()
        plt.show()
'''
# EJEMPLO DE USO (puedes comentar esto cuando lo integres al código general):
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
modelo = RegresionLineal(x, y)
modelo.calcular()
modelo.graficar()'''
