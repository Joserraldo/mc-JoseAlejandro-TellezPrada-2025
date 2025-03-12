import sympy as sp
x = sp.symbols('x')
f1 = 0.3*x**3 - 1.8*x**2 + 2.5*x - 1
base_1 = 0.4

taylor_f1 = sp.series(f1, x, base_1, 4).removeO()
valor_f1 = taylor_f1.subs(x, 0.5)

print(f"Predicción de f(0.5) si f(x) = 0.3x^3 - 1.8x^2 + 2.5^x - 1, usando como base x=0.4\n para la primera función: {valor_f1}")

f2 = 1.4*sp.exp(x) - 3.2*x + 2.4
#exp es la función exponencial
base_2 = 0.6

taylor_f2 = sp.series(f2, x, base_2, 4).removeO()

valor_f2 = taylor_f2.subs(x, 0.65)
print(f"Predicción de f(0.65) si f(x) = 1,4e^x - 3.2x + 2.4, usando como base x=0.6\n para la segunda función: {valor_f2}")
