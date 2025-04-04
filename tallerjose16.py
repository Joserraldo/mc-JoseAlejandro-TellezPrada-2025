from fractions import Fraction

def formato_fraccion(f):
    """Mejora la presentación de las fracciones"""
    return str(f.numerator) if f.denominator == 1 else f"{f.numerator}/{f.denominator}"

def imprimirMatriz(matriz, titulo):
    print(titulo)
    for fila in matriz:
        print("[" + " ".join(f"{formato_fraccion(x):>5}" for x in fila) + "]")
    print()

def matrizIdentidad(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]

def matrizInversa(a):
    n = len(a)
    a = [[Fraction(x) for x in fila] for fila in a]  # Convertir a fracciones
    b = matrizIdentidad(n)
    
    for i in range(n):
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    break
            else:
                raise ValueError("La matriz no es invertible")
        
        pivote = a[i][i]
        a[i] = [x / pivote for x in a[i]]
        b[i] = [x / pivote for x in b[i]]

        for k in range(n):
            if i != k:
                factor = a[k][i]
                a[k] = [x - factor * y for x, y in zip(a[k], a[i])]
                b[k] = [x - factor * y for x, y in zip(b[k], b[i])]
    
    return b

def multiplicarMatrices(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def main():
    try:
        # Matriz A
        a1 = [
            [Fraction(3), Fraction(2), Fraction(2)],
            [Fraction(3), Fraction(1), Fraction(-3)],
            [Fraction(1), Fraction(0), Fraction(-2)]
        ]
        print("Calculando inversa de la matriz A:")
        inv_a1 = matrizInversa(a1)
        imprimirMatriz(a1, "Matriz A:")
        imprimirMatriz(inv_a1, "Inversa de A:")
        
        # Verificar A * A^-1 = I
        producto = multiplicarMatrices(a1, inv_a1)
        imprimirMatriz(producto, "Verificación A * A^-1:")
        
        # Matriz B
        a2 = [
            [Fraction(1), Fraction(2), Fraction(0), Fraction(4)],
            [Fraction(2), Fraction(0), Fraction(-1), Fraction(-2)],
            [Fraction(1), Fraction(1), Fraction(-1), Fraction(0)],
            [Fraction(0), Fraction(4), Fraction(1), Fraction(0)]
        ]
        print("Calculando inversa de la matriz B:")
        inv_a2 = matrizInversa(a2)
        imprimirMatriz(a2, "Matriz B:")
        imprimirMatriz(inv_a2, "Inversa de B:")
        
        # Verificar B * B^-1 = I
        producto = multiplicarMatrices(a2, inv_a2)
        imprimirMatriz(producto, "Verificación B * B^-1:")
        
    except Exception as e:
        print("Error:", e)

main()
