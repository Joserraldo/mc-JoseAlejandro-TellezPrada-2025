import sympy as sp
from math import pi
def error_func1(x_val, dx):
    x = sp.symbols('x')
    
    funcion = 1.1 * x**4 - 1.9 * x**3 + 1.2 * x**2 - 2 * x + 4
    #dif es para derivar
    fPrima = sp.diff(funcion, x) 
    #subs remplazamos por el valor que nos dan
    f_prima_val = fPrima.subs(x, x_val)
    delta_f = abs(f_prima_val) * dx  
    return delta_f

def error_func2(x_val, dx):
    x = sp.symbols('x')
    
    funcion2 = sp.cos(x) * sp.ln(2*x)   
    f_prime = sp.diff(funcion2, x)
    f_prime_val = f_prime.subs(x, x_val)
    
    delta_f = abs(f_prime_val) * dx
    return delta_f

x1 = 1.4
dx1 = 0.05
error1 = error_func1(x1, dx1)
print(f"El error estimado en f(x) para x = {x1} y ∆x = {dx1} es: {error1:.6f}")

x2 = pi / 3
dx2 = 0.005
error2 = error_func2(x2, dx2)
print(f"El error estimado en f(x) para x = π/3 y ∆x = {dx2} es: {error2:.6f}")
