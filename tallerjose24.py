import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

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

def main():
    x = [1, 2, 3, 4, 5]
    y = [2, 0.5, -2, -3.5, 0.5]
    x = [Fraction(i) for i in x]
    y = [Fraction(i) for i in y]

    n = len(x)
    polinomio_final = [Fraction(0)]

    for i in range(n):
        numerador = [Fraction(1)]
        denominador = Fraction(1)
        for j in range(n):
            if i != j:
                numerador = multiplicar_polinomio(numerador, [-x[j], 1])
                denominador *= (x[i] - x[j])
        li = [(coef * y[i]) / denominador for coef in numerador]
        polinomio_final = sumar_polinomios(polinomio_final, li)

    grado = len(polinomio_final) - 1
    expresion = ""
    for i, coef in enumerate(reversed(polinomio_final)):
        if coef == 0:
            continue
        signo = " + " if coef > 0 and expresion else (" - " if coef < 0 else "")
        valor = abs(coef)
        exponente = grado - i
        if exponente == 0:
            expresion += f"{signo}{valor}"
        elif exponente == 1:
            expresion += f"{signo}{valor}x"
        else:
            expresion += f"{signo}{valor}x^{exponente}"

    print("Polinomio de Lagrange:")
    print("f(x) =", expresion)
   
    xs = np.linspace(float(min(x)) - 1, float(max(x)) + 1, 400)
    
    coefs_float = [float(c) for c in reversed(polinomio_final)]
    ys = np.polyval(coefs_float, xs)
    
    plt.figure(figsize=(10, 6))
    plt.plot(xs, ys, label="Polinomio de Lagrange", color='blue')
    plt.scatter([float(i) for i in x], [float(i) for i in y], color='red', zorder=5, label="Puntos dados")
    plt.title("Interpolación de Lagrange")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.legend()
    
    plt.text(min(xs), max(ys)*0.9, f"f(x) = {expresion}", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

    plt.show()

main()
