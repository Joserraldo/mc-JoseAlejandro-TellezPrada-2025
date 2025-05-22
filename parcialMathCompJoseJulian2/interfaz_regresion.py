import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from regresion_polinomial import RegresionPolinomialGeneral

class InterfazRegresion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Regresión Polinomial")
        self.root.geometry("900x750+0+0")
        self.titulo = tk.Label(self.root, text="REGRESIÓN POLINOMIAL", font=("Helvetica", 20, "bold"))
        self.titulo.pack(pady=10)
        self.subtitulo = tk.Label(self.root, text="By José Alejandro Téllez Prada & Julian David Lizcano Manrique", font=("Helvetica", 12))
        self.subtitulo.pack(pady=0)
        self.frame_entradas = tk.Frame(self.root)
        self.frame_entradas.pack(pady=10)

        self.entradas_x = []
        self.entradas_y = []

        tk.Label(self.frame_entradas, text="X").grid(row=0, column=0)
        tk.Label(self.frame_entradas, text="Y").grid(row=0, column=1)

        for _ in range(6):
            self.agregar_fila()

        self.frame_r2 = tk.Frame(self.root)
        self.frame_r2.pack(pady=10)
        tk.Label(self.frame_r2, text="R² objetivo:").pack(side=tk.LEFT)
        self.r2_entry = tk.Entry(self.frame_r2, width=5)
        self.r2_entry.insert(0, "0.95")
        self.r2_entry.pack(side=tk.LEFT)

        self.btn_regresion = tk.Button(self.root, text="Buscar mejor regresión", command=self.buscar_mejor_regresion)
        self.btn_regresion.pack(pady=10)

        # Frame para la gráfica y botones de navegación
        self.frame_grafica = tk.Frame(self.root)
        self.frame_grafica.pack(fill=tk.BOTH, expand=True)

        self.canvas = None
        self.figuras = []
        self.indice_figura = 0

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=5)
        self.btn_anterior = tk.Button(self.frame_botones, text="Anterior", command=self.mostrar_anterior, state=tk.DISABLED)
        self.btn_anterior.pack(side=tk.LEFT, padx=10)
        self.btn_siguiente = tk.Button(self.frame_botones, text="Siguiente", command=self.mostrar_siguiente, state=tk.DISABLED)
        self.btn_siguiente.pack(side=tk.LEFT, padx=10)

        self.root.mainloop()

    def agregar_fila(self):
        fila = len(self.entradas_x)
        entrada_x = tk.Entry(self.frame_entradas, width=10)
        entrada_y = tk.Entry(self.frame_entradas, width=10)

        entrada_x.grid(row=fila + 1, column=0)
        entrada_y.grid(row=fila + 1, column=1)

        entrada_x.bind("<KeyRelease>", lambda e: self.verificar_filas())
        entrada_y.bind("<KeyRelease>", lambda e: self.verificar_filas())

        self.entradas_x.append(entrada_x)
        self.entradas_y.append(entrada_y)

    def verificar_filas(self):
        for i in range(len(self.entradas_x)):
            entrada_x = self.entradas_x[i]
            entrada_y = self.entradas_y[i]

            x_val = entrada_x.get().strip()
            y_val = entrada_y.get().strip()

            if x_val and y_val:
                entrada_x.config(bg="#e6ffe6")  # Verde claro
                entrada_y.config(bg="#e6ffe6")
            else:
                entrada_x.config(bg="white")
                entrada_y.config(bg="white")

        # Si la última fila está llena, agregamos una nueva
        if self.entradas_x and self.entradas_y:
            x_ult = self.entradas_x[-1].get().strip()
            y_ult = self.entradas_y[-1].get().strip()
            if x_ult and y_ult:
                self.agregar_fila()

    def buscar_mejor_regresion(self):
        try:
            x = []
            y = []

            for ex, ey in zip(self.entradas_x, self.entradas_y):
                x_str = ex.get().strip()
                y_str = ey.get().strip()
                if x_str != "" and y_str != "":
                    x.append(float(x_str))
                    y.append(float(y_str))

            if len(x) < 6:
                messagebox.showerror("Error", "Debes ingresar al menos 6 pares de datos.")
                return

            if len(set(x)) != len(x):
                messagebox.showerror("Error", f"Los valores en X no deben repetirse para la regresión polinomial.")
                return

            r2_objetivo = float(self.r2_entry.get())
            self.generar_figuras_regresion(x, y, r2_objetivo)

        except ValueError:
            messagebox.showerror("Error", "Asegúrate de ingresar solo números válidos.")

    def generar_figuras_regresion(self, x, y, r2_objetivo=0.95):
        self.figuras = []
        max_grado = len(x) - 1
        for grado in range(1, max_grado + 1):
            modelo = RegresionPolinomialGeneral(x, y, grado)
            modelo.calcular()
            fig = self.crear_figura(modelo, x, y)
            self.figuras.append(fig)
            if modelo.r2 >= r2_objetivo:
                break
        self.indice_figura = 0
        self.mostrar_figura_actual()

    def crear_figura(self, modelo, x, y):
        coef = modelo.coeficientes
        g = modelo.grado
        a_texto = " + ".join(
            f"{coef[k]:.4f}x^{k}" if k > 0 else f"{coef[k]:.4f}" for k in range(len(coef))
        )
        a_texto = a_texto.replace("x^1", "x")

        fig, ax = plt.subplots(figsize=(7, 4))
        ax.scatter(x, y, color="red", label="Datos originales")

        x_suave = np.linspace(min(x), max(x), 300)
        y_suave = sum(coef[k] * x_suave**k for k in range(g + 1))

        ax.plot(x_suave, y_suave, color="blue", label=f"y = {a_texto}")
        ax.set_title(f"Regresión Polinomial de Grado {g}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        ax.legend()

        texto = (
            f"Ecuación: y = {a_texto}\n"
            f"R² = {modelo.r2:.4f}\n"
            f"r = {modelo.r:.2f}%\n"
            f"sy = {modelo.sy:.4f}\n"
            f"sy/x = {modelo.sy_x:.4f}"
        )
        fig.text(0.5, 0.01, texto, ha="center", fontsize=10, bbox={"facecolor": "white", "alpha": 0.8})
        fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        return fig

    def mostrar_figura_actual(self):
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        if not self.figuras:
            self.btn_anterior.config(state=tk.DISABLED)
            self.btn_siguiente.config(state=tk.DISABLED)
            return
        fig = self.figuras[self.indice_figura]
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.actualizar_botones()

    def mostrar_anterior(self):
        if self.indice_figura > 0:
            self.indice_figura -= 1
            self.mostrar_figura_actual()

    def mostrar_siguiente(self):
        if self.indice_figura < len(self.figuras) - 1:
            self.indice_figura += 1
            self.mostrar_figura_actual()

    def actualizar_botones(self):
        self.btn_anterior.config(state=tk.NORMAL if self.indice_figura > 0 else tk.DISABLED)
        self.btn_siguiente.config(state=tk.NORMAL if self.indice_figura < len(self.figuras) - 1 else tk.DISABLED)


