import sympy as sp

# Definimos la función y sus parámetros
x = sp.symbols("x")
f = 0.25 * x**4 - 0.75 * x**2 + 4.5
xi = 0.6
h = 0.1

# Calculamos valores de la función en diferentes puntos
f_xi = f.subs(x, xi)
f_xi_plus_h = f.subs(x, xi + h)
f_xi_minus_h = f.subs(x, xi - h)
f_xi_plus_2h = f.subs(x, xi + 2*h)
f_xi_minus_2h = f.subs(x, xi - 2*h)

print("EJERCICIO 1: x = 0.6, h = 0.1")
print("-" * 50)

# PRIMERA DERIVADA
print("PRIMERA DERIVADA:")
print("-" * 50)

# Diferencia finita hacia adelante
primera_adelante = (f_xi_plus_h - f_xi) / h
print(f"Diferencia hacia adelante: {primera_adelante}")

# Diferencia finita hacia atrás
primera_atras = (f_xi - f_xi_minus_h) / h
print(f"Diferencia hacia atrás: {primera_atras}")

# Diferencia finita centrada
primera_centrada = (f_xi_plus_h - f_xi_minus_h) / (2 * h)
print(f"Diferencia centrada: {primera_centrada}")

# Valor verdadero de la primera derivada
primera_verdadera = sp.diff(f, x).subs(x, xi)
print(f"Valor verdadero: {primera_verdadera}")
print(f"Error (adelante): {(primera_adelante - primera_verdadera)}")
print(f"Error (atrás): {(primera_atras - primera_verdadera)}")
print(f"Error (centrada): {(primera_centrada - primera_verdadera)}\n")

# SEGUNDA DERIVADA
print("SEGUNDA DERIVADA:")
print("-" * 50)

# Diferencia finita hacia adelante
segunda_adelante = (f_xi_plus_2h - 2*f_xi_plus_h + f_xi) / (h**2)
print(f"Diferencia hacia adelante: {segunda_adelante}")

# Diferencia finita hacia atrás
segunda_atras = (f_xi - 2*f_xi_minus_h + f_xi_minus_2h) / (h**2)
print(f"Diferencia hacia atrás: {segunda_atras}")

# Diferencia finita centrada
segunda_centrada = (f_xi_plus_h - 2*f_xi + f_xi_minus_h) / (h**2)
print(f"Diferencia centrada: {segunda_centrada}")

# Valor verdadero de la segunda derivada
segunda_verdadera = sp.diff(f, x, 2).subs(x, xi)
print(f"Valor verdadero: {segunda_verdadera}")
print(f"Error (adelante): {(segunda_adelante - segunda_verdadera)}")
print(f"Error (atrás): {(segunda_atras - segunda_verdadera)}")
print(f"Error (centrada): {(segunda_centrada - segunda_verdadera)}")
print()

# EJERCICIO 2: Calcular con h = 0.05
print("EJERCICIO 2: x = 0.6, h = 0.05")
print("-" * 50)

h2 = 0.05
f_xi = f.subs(x, xi)
f_xi_plus_h2 = f.subs(x, xi + h2)
f_xi_minus_h2 = f.subs(x, xi - h2)

# Primera derivada centrada con h = 0.05
primera_centrada_h2 = (f_xi_plus_h2 - f_xi_minus_h2) / (2 * h2)
print(f"Primera derivada (centrada) con h = 0.05: {primera_centrada_h2}")
print(f"Error: {(primera_centrada_h2 - primera_verdadera)}")
print()

# Segunda derivada centrada con h = 0.05
segunda_centrada_h2 = (f_xi_plus_h2 - 2*f_xi + f_xi_minus_h2) / (h2**2)
print(f"Segunda derivada (centrada) con h = 0.05: {segunda_centrada_h2}")
print(f"Error: {(segunda_centrada_h2 - segunda_verdadera)}")
print()

# Comparación de resultados
print("COMPARACIÓN DE RESULTADOS:")
print("-" * 50)
print(f"Error en primera derivada centrada (h = 0.1): {(primera_centrada - primera_verdadera)}")
print(f"Error en primera derivada centrada (h = 0.05): {(primera_centrada_h2 - primera_verdadera)}")
print(f"Error en segunda derivada centrada (h = 0.1): {(segunda_centrada - segunda_verdadera)}")
print(f"Error en segunda derivada centrada (h = 0.05): {(segunda_centrada_h2 - segunda_verdadera)}\n")
print("CONCLUSIÓN:")
print("-" * 50)
print("Se observa que el resultado obtenido con h = 0.05 es más preciso que el obtenido con h = 0.1.\nEsto se debe a que cuando h es más pequeño, las aproximaciones por diferencias finitas \nacercan más al valor verdadero de la derivada. En general, al reducir el tamaño de \nel error de truncamiento disminuye, aunque hay un límite práctico debido a errores \nredondeo en cálculos computacionales (no evidentes en este ejemplo).")