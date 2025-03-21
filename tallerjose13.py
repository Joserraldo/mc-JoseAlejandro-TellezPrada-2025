import math
import sympy as sp

def calc_taylor(x0, x, orden_max):

    actual = math.exp(-x)  
    anterior = 0
    errores = []
    
    X = sp.Symbol('X')
    func = sp.exp(-X)
    
    for i in range(orden_max + 1):
        termino = func.series(X, x0, i+1).removeO()  
        anterior = termino.subs(X, x)  
        error = abs((actual - anterior) / actual) * 100
        errores.append((i, float(anterior), float(error)))
    
    return errores

x0 = 0.8
x = 0.805
orden_max = 15

resultados = calc_taylor(x0, x, orden_max)

print("Orden |          Aproximación     |    Error %")
print("---------------------------------------")
for orden, aprox, error in resultados:
    print(f"{orden:5} | {aprox:.23f} | {error:10}")

