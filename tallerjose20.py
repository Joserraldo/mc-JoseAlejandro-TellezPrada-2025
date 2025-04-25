import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, exp

def analisis_regresion_completo(x, y):
   
    def regresion_lineal(x, y):
        n = len(x)
        media_x = np.mean(x)
        media_y = np.mean(y)
        
        suma_xy = np.sum(x * y)
        suma_x = np.sum(x)
        suma_y = np.sum(y)
        suma_x_cuadrado = np.sum(x**2)
        
        a1 = (n * suma_xy - suma_x * suma_y) / (n * suma_x_cuadrado - suma_x**2)
        a0 = media_y - a1 * media_x
        
        y_pred = a0 + a1 * x
        
        st = np.sum((y - media_y)**2)
        sr = np.sum((y - y_pred)**2)
        
        sy = np.sqrt(st / (n - 1))
        sy_x = np.sqrt(sr / (n - 2))
        
        r_cuadrado = 1 - (sr / st)
        r = sqrt(r_cuadrado) * 100
        
        return {
            'tipo': 'Lineal',
            'ecuacion': f'y = {a0:.4f} + {a1:.4f}x',
            'y_pred': y_pred,
            'r_cuadrado': r_cuadrado,
            'r': r,
            'sy': sy,
            'sy_x': sy_x,
            'parametros': (a0, a1)
        }
    
    
    def regresion_exponencial(x, y):
        n = len(x)
        ln_y = np.log(y)
        
        media_x = np.mean(x)
        media_ln_y = np.mean(ln_y)
        
        suma_x_ln_y = np.sum(x * ln_y)
        suma_x = np.sum(x)
        suma_ln_y = np.sum(ln_y)
        suma_x_cuadrado = np.sum(x**2)
        
        beta = (n * suma_x_ln_y - suma_x * suma_ln_y) / (n * suma_x_cuadrado - suma_x**2)
        ln_alpha = media_ln_y - beta * media_x
        alpha = exp(ln_alpha)
        
        ln_y_pred = ln_alpha + beta * x
        y_pred = alpha * np.exp(beta * x)
        
        st = np.sum((ln_y - media_ln_y)**2)
        sr = np.sum((ln_y - ln_y_pred)**2)
        
        sy = np.sqrt(st / (n - 1))
        sy_x = np.sqrt(sr / (n - 2))
        
        r_cuadrado = 1 - (sr / st)
        r = sqrt(r_cuadrado) * 100
        
        return {
            'tipo': 'Exponencial',
            'ecuacion': f'y = {alpha:.4f}e^({beta:.4f}x)',
            'y_pred': y_pred,
            'r_cuadrado': r_cuadrado,
            'r': r,
            'sy': sy,
            'sy_x': sy_x,
            'parametros': (alpha, beta)
        }
    
    
    def regresion_potencias(x, y):
        n = len(x)
        ln_x = np.log(x)
        ln_y = np.log(y)
        
        media_ln_x = np.mean(ln_x)
        media_ln_y = np.mean(ln_y)
        
        suma_ln_x_ln_y = np.sum(ln_x * ln_y)
        suma_ln_x = np.sum(ln_x)
        suma_ln_y = np.sum(ln_y)
        suma_ln_x_cuadrado = np.sum(ln_x**2)
        
        beta = (n * suma_ln_x_ln_y - suma_ln_x * suma_ln_y) / (n * suma_ln_x_cuadrado - suma_ln_x**2)
        ln_alpha = media_ln_y - beta * media_ln_x
        alpha = exp(ln_alpha)
        
        ln_y_pred = ln_alpha + beta * ln_x
        y_pred = alpha * np.power(x, beta)
        
        st = np.sum((ln_y - media_ln_y)**2)
        sr = np.sum((ln_y - ln_y_pred)**2)
        
        sy = np.sqrt(st / (n - 1))
        sy_x = np.sqrt(sr / (n - 2))
        
        r_cuadrado = 1 - (sr / st)
        r = sqrt(r_cuadrado) * 100
        
        return {
            'tipo': 'Potencias',
            'ecuacion': f'y = {alpha:.4f}x^{beta:.4f}',
            'y_pred': y_pred,
            'r_cuadrado': r_cuadrado,
            'r': r,
            'sy': sy,
            'sy_x': sy_x,
            'parametros': (alpha, beta)
        }
    
    
    def regresion_razon_crecimiento(x, y):
        n = len(x)
        inv_y = 1 / y
        exp_neg_x = np.exp(-x)
        
        media_exp_neg_x = np.mean(exp_neg_x)
        media_inv_y = np.mean(inv_y)
        
        suma_exp_neg_x_inv_y = np.sum(exp_neg_x * inv_y)
        suma_exp_neg_x = np.sum(exp_neg_x)
        suma_inv_y = np.sum(inv_y)
        suma_exp_neg_x_cuadrado = np.sum(exp_neg_x**2)
        
        b = (n * suma_exp_neg_x_inv_y - suma_exp_neg_x * suma_inv_y) / (n * suma_exp_neg_x_cuadrado - suma_exp_neg_x**2)
        a = media_inv_y - b * media_exp_neg_x
        
        inv_y_pred = a + b * exp_neg_x
        y_pred = 1 / inv_y_pred
        
        st = np.sum((inv_y - media_inv_y)**2)
        sr = np.sum((inv_y - inv_y_pred)**2)
        
        sy = np.sqrt(st / (n - 1))
        sy_x = np.sqrt(sr / (n - 2))
        
        r_cuadrado = 1 - (sr / st)
        r = sqrt(r_cuadrado) * 100
        
        return {
            'tipo': 'Razón de Crecimiento',
            'ecuacion': f'y = 1/({a:.4f} + {b:.4f}e^(-x))',
            'y_pred': y_pred,
            'r_cuadrado': r_cuadrado,
            'r': r,
            'sy': sy,
            'sy_x': sy_x,
            'parametros': (a, b, 1)  
        }
    
    
    resultados = [
        regresion_lineal(x, y),
        regresion_exponencial(x, y),
        regresion_potencias(x, y),
        regresion_razon_crecimiento(x, y)
    ]
    
    
    resultados_ordenados = sorted(resultados, key=lambda x: x['r_cuadrado'], reverse=True)
    
    return resultados, resultados_ordenados


x = np.array([1, 2, 3, 4, 5,6,7,8])
y = np.array([4.5, 6.5, 7.5, 8, 8.4,8.8,9,9.3])


resultados, resultados_ordenados = analisis_regresion_completo(x, y)


colores = ['blue', 'red', 'green', 'purple']


fig, axs = plt.subplots(2, 2, figsize=(15, 12))
axs = axs.flatten()


for i, resultado in enumerate(resultados):
    ax = axs[i]
    ax.scatter(x, y, color='black', label='Datos originales')
    ax.plot(x, resultado['y_pred'], color=colores[i], linewidth=2, 
            label=f"Modelo {resultado['tipo']}: {resultado['ecuacion']}")
    
    info = (f"R² = {resultado['r_cuadrado']:.4f}\n"
            f"r = {resultado['r']:.2f}%\n"
            f"Sy = {resultado['sy']:.4f}\n"
            f"Sy/x = {resultado['sy_x']:.4f}")
    
    ax.text(0.05, 0.95, info, transform=ax.transAxes, 
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    ax.set_title(f"Modelo {resultado['tipo']}")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.grid(True)
    ax.legend()

fig.suptitle('Comparación de los Cuatro Modelos de Regresión', fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.96])


plt.figure(figsize=(10, 8))
plt.scatter(x, y, color='black', label='Datos originales', s=50)

for i, resultado in enumerate(resultados):
    plt.plot(x, resultado['y_pred'], color=colores[i], linewidth=2, 
             label=f"{resultado['tipo']} (R² = {resultado['r_cuadrado']:.4f})")

plt.title('Comparación de los Cuatro Modelos de Regresión')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend()

mejor_modelo = resultados_ordenados[0]

fig, ax = plt.subplots(figsize=(14, 6))
ax.axis('off')
ax.axis('tight')

tabla_datos = []
encabezados = ['Modelo', 'Ecuación', 'R²', 'r (%)', 'Sy', 'Sy/x']

for res in resultados_ordenados:
    fila = [
        res['tipo'],
        res['ecuacion'],
        f"{res['r_cuadrado']:.4f}",
        f"{res['r']:.2f}%",
        f"{res['sy']:.4f}",
        f"{res['sy_x']:.4f}"
    ]
    tabla_datos.append(fila)

tabla = ax.table(cellText=tabla_datos,
                colLabels=encabezados,
                loc='center',
                cellLoc='center',
                colColours=['#f2f2f2']*len(encabezados))

tabla.auto_set_font_size(False)
tabla.set_fontsize(10)
tabla.scale(1.2, 1.5)

for j in range(len(encabezados)):
    tabla[(1, j)].set_facecolor('#c6efce')

plt.suptitle('Comparación de Modelos de Regresión (Ordenados por R²)', fontsize=14)
plt.title(f"El modelo más preciso es: {mejor_modelo['tipo']} con R² = {mejor_modelo['r_cuadrado']:.4f}", fontsize=12, color='green')
plt.tight_layout()

print("\n====== RESULTADOS DE LA COMPARACIÓN ======")
print(f"El modelo más preciso es: {mejor_modelo['tipo']} con R² = {mejor_modelo['r_cuadrado']:.4f}")
print(f"Ecuación: {mejor_modelo['ecuacion']}")
print("\nResumen de todos los modelos (ordenados por precisión):")
for i, res in enumerate(resultados_ordenados):
    print(f"{i+1}. {res['tipo']}: R² = {res['r_cuadrado']:.4f}, r = {res['r']:.2f}%, Ecuación: {res['ecuacion']}")

plt.show()