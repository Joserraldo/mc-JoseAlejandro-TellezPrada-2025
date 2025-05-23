import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def agregar_valor(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._agregar_recursivo(self.raiz, valor)
    
    def _agregar_recursivo(self, nodo_actual, valor):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.izquierdo, valor)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(valor)
            else:
                self._agregar_recursivo(nodo_actual.derecho, valor)
        
    
    def buscar_valor(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo_actual, valor):
        if nodo_actual is None:
            return False
        if valor == nodo_actual.valor:
            return True
        elif valor < nodo_actual.valor:
            return self._buscar_recursivo(nodo_actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, valor)
    
    def imprimir_ascendente(self):
        elementos = []
        self._recorrido_inorden(self.raiz, elementos)
        return elementos
    
    def _recorrido_inorden(self, nodo_actual, elementos):
        if nodo_actual is not None:
            self._recorrido_inorden(nodo_actual.izquierdo, elementos)
            elementos.append(nodo_actual.valor)
            self._recorrido_inorden(nodo_actual.derecho, elementos)
    
    def imprimir_estructura(self):
        def _imprimir_nodo(nodo, prefijo="", es_izquierdo=True):
            if nodo is not None:
                if nodo.derecho is not None:
                    new_prefijo = prefijo + ("│   " if es_izquierdo else "    ")
                    _imprimir_nodo(nodo.derecho, new_prefijo, False)
                
                print(prefijo + ("└── " if es_izquierdo else "┌── ") + str(nodo.valor))
                
                if nodo.izquierdo is not None:
                    new_prefijo = prefijo + ("    " if es_izquierdo else "│   ")
                    _imprimir_nodo(nodo.izquierdo, new_prefijo, True)

        _imprimir_nodo(self.raiz)


    def _formatear_nodo(self, nodo):
        if nodo is None:
            return [], 0, 0, 0

        linea_valor = str(nodo.valor)
        ancho = len(linea_valor)
        
        izq_lines, izq_ancho, izq_altura, izq_raiz = self._formatear_nodo(nodo.izquierdo)
        
        der_lines, der_ancho, der_altura, der_raiz = self._formatear_nodo(nodo.derecho)

        altura = max(izq_altura, der_altura)
        nueva_altura = altura + 2
        
        primer_linea = (" " * izq_raiz) + (" " * (izq_ancho - izq_raiz)) + linea_valor + (" " * der_raiz) + (" " * (der_ancho - der_raiz))
        segunda_linea = (
            (" " * izq_raiz) +
            ("/" if nodo.izquierdo else " ") +
            (" " * (izq_ancho - izq_raiz + ancho + der_raiz - 1)) +
            ("\\" if nodo.derecho else " ")
        )

        combined_lines = []
        for i in range(altura):
            izquierda = izq_lines[i] if i < len(izq_lines) else " " * izq_ancho
            derecha = der_lines[i] if i < len(der_lines) else " " * der_ancho
            combined_lines.append(izquierda + (" " * ancho) + derecha)

        return [primer_linea, segunda_linea] + combined_lines, izq_ancho + ancho + der_ancho, nueva_altura, izq_ancho + ancho // 2


def generar_numeros_aleatorios():
    numeros = set()
    while len(numeros) < 20:
        numeros.add(random.randint(1, 100))
    return list(numeros)

def mostrar_menu():
    print("\n" + "="*50)
    print("ÁRBOL DE BÚSQUEDA BINARIA - TALLER 26")
    print("="*50)
    print("1. Generar nuevo árbol con 20 números aleatorios")
    print("2. Buscar un número en el árbol")
    print("3. Mostrar números en orden ascendente")
    print("4. Mostrar estructura del árbol")
    print("5. Agregar un número manualmente")
    print("6. Salir")
    print("="*50)

def main():
    arbol = ArbolBinario()
    numeros_generados = []
    
    print("¡Bienvenido al programa de Árbol de Búsqueda Binaria!")
    
    while True:
        mostrar_menu()
        
        try:
            opcion = input("Seleccione una opción (1-6): ").strip()
            
            if opcion == "1":
                print("\nGenerando 20 números aleatorios diferentes...")
                numeros_generados = generar_numeros_aleatorios()
                
                arbol = ArbolBinario()
                
                random.shuffle(numeros_generados) 
                for numero in numeros_generados:
                    arbol.agregar_valor(numero)

                print(f"Números generados: {(numeros_generados)}")
                print("¡Árbol creado exitosamente!")
                
            elif opcion == "2":
                if arbol.raiz is None:
                    print("\n¡Error! Primero debe generar un árbol (opción 1)")
                    continue
                
                try:
                    numero = int(input("\nIngrese el número a buscar: "))
                    if arbol.buscar_valor(numero):
                        print(f"✓ El número {numero} SÍ se encuentra en el árbol")
                    else:
                        print(f"✗ El número {numero} NO se encuentra en el árbol")
                except ValueError:
                    print("¡Error! Debe ingresar un número válido")
                
            elif opcion == "3":
                if arbol.raiz is None:
                    print("\n¡Error! Primero debe generar un árbol (opción 1)")
                    continue
                
                elementos_ascendentes = arbol.imprimir_ascendente()
                print(f"\nElementos en orden ascendente:")
                print(f"{elementos_ascendentes}")
                
            elif opcion == "4":
                if arbol.raiz is None:
                    print("\n¡Error! Primero debe generar un árbol (opción 1)")
                    continue
                
                print(f"\nEstructura del árbol:")
                print(f"Números originales: {(numeros_generados) if numeros_generados else 'No disponible'}")
                print("\nRepresentación visual:")
                arbol.imprimir_estructura()
                
            elif opcion == "5":
                if arbol.raiz is None:
                    print("\n¡Error! Primero debe generar un árbol (opción 1)")
                    continue
                
                try:
                    numero = int(input("\nIngrese el número a agregar: "))
                    if arbol.buscar_valor(numero):
                        print(f"El número {numero} ya existe en el árbol")
                    else:
                        arbol.agregar_valor(numero)
                        print(f"✓ Número {numero} agregado exitosamente")
                except ValueError:
                    print("¡Error! Debe ingresar un número válido")
                
            elif opcion == "6":
                print("\n¡Gracias por usar el programa!")
                print("Desarrollado para Taller 26 - Árbol de Búsqueda Binaria")
                break
                
            else:
                print("\n¡Opción no válida! Seleccione una opción del 1 al 6")
                
        except KeyboardInterrupt:
            print("\n\n¡Programa interrumpido por el usuario!")
            break
        except Exception as e:
            print(f"\n¡Error inesperado! {str(e)}")

if __name__ == "__main__":
    main()