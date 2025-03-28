import copy
from fractions import Fraction

def imprimirSistema(a, b, etiqueta):
    n = len(b)
    print(etiqueta)
    for i in range(n):
        for j in range(n):
            print(a[i][j], end = " ")
        print("|", b[i])
    print()

def gaussJordan(ao, bo):
    a = copy.deepcopy(ao)
    b = copy.copy(bo)

    n = len(b)
    imprimirSistema(a, b, "Matriz inicial")

    for i in range(n):
        # Si el pivote es cero, buscar una fila para intercambiar
        if a[i][i] == 0:
            for k in range(i+1, n):
                if a[k][i] != 0:
                    # Intercambiar filas
                    a[i], a[k] = a[k], a[i]
                    b[i], b[k] = b[k], b[i]
                    print(f"Se intercambiaron las filas {i} y {k}")
                    break

        # Dividir por el pivote
        pivote = Fraction(a[i][i])
        for j in range(n):
            a[i][j] = Fraction(a[i][j], pivote)
        b[i] = Fraction(b[i], pivote)
        imprimirSistema(a, b, "División")

        # Reducción
        for k in range(n):
            if i != k:
                # Se reduce
                valorAux = -a[k][i]
                for j in range(n):
                    a[k][j] += a[i][j] * valorAux
                b[k] += b[i] * valorAux
        imprimirSistema(a, b, "Reducción")
    
    return b

try: 
    a = [[2, 0, 2], [4, 0, -1], [3, 2, -2]]
    b = [7, 18, 16]
    x = gaussJordan(a, b)

    print("Respuesta:")
    for i in range(len(x)):
        print("x" + str(i+1), "=", x[i])

    #Pruebas
    print("\nPruebas:")
    for i in range(len(b)):
        valorAux = b[i]
        for j in range(len(b)):
            valorAux -= a[i][j] * x[j]
        print("Test", i + 1, "=", valorAux)
except Exception as e:
    print("Error: ", str(e), "sistema mal condicionado, presenta un error")