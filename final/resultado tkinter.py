import tkinter as tk
from tkinter import messagebox
import re
from operar_enteros import OperarEnteros
from operar_flotantes import OperarFlotantes

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto Matemáticas Computacionales")
        self.root.geometry("600x450")
        
        self.entero_operador = OperarEnteros()
        self.flotante_operador = OperarFlotantes()
        
        self.titulo = tk.Label(self.root, text="Proyecto Matemáticas Computacionales", font=("Arial", 16, "bold"))
        self.titulo.pack(pady=10)
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)
        
        self.label = tk.Label(self.frame, text="Ingrese operación (ej. 4.5+5/2-8):")
        self.label.grid(row=0, column=0)
        
        self.entry = tk.Entry(self.frame, width=40)
        self.entry.grid(row=0, column=1)
        
        self.btn_calcular = tk.Button(self.frame, text="Calcular", command=self.calcular_operacion)
        self.btn_calcular.grid(row=1, column=0, columnspan=2, pady=10)
        
        self.label_resultado = tk.Label(self.frame, text="Resultado:")
        self.label_resultado.grid(row=2, column=0, columnspan=2)
        
        self.label_binario = tk.Label(self.frame, text="Binario:")
        self.label_binario.grid(row=3, column=0, columnspan=2)
        
        self.autores = tk.Label(self.root, text="Julian David Lizcano Manrique - U00180133\nJosé Alejandro Téllez Prada- U00060479", font=("Arial", 10))
        self.autores.pack(side=tk.BOTTOM, pady=10)
    
    def es_decimal(self, valor):
        """Determina si un valor es decimal o entero"""
        if isinstance(valor, str):
            # Manejar números negativos
            if valor.startswith('-'):
                valor = valor[1:]
            return '.' in valor and not valor.endswith('.0')
        elif isinstance(valor, float):
            return not valor.is_integer()
        return False

    def realizar_operacion(self, a, b, operador):
        """Realiza operación decidiendo entre enteros y flotantes"""
        # Convertir a float solo si realmente son decimales
        usar_flotantes = self.es_decimal(a) or self.es_decimal(b)
        
        if usar_flotantes:
            a = float(a)
            b = float(b)
            
            flotantes = OperarFlotantes([a, b])
            if operador == '*':
                resultado = flotantes.operar_todos('multiplicacion')
                return flotantes.formatear_flotante(resultado)
            elif operador == '/':
                resultado = flotantes.operar_todos('division')
                return flotantes.formatear_flotante(resultado)
        else:
            # Operación de enteros (asegurarse de que son enteros)
            a_int = int(float(a))  # Primero convertir a float por si viene como string "5.0"
            b_int = int(float(b))
            
            enteros = OperarEnteros([a_int, b_int])
            if operador == '*':
                resultado = enteros.operar_todos('multiplicacion')
                return int(resultado, 2)
            elif operador == '/':
                resultado = enteros.operar_todos('division')
                return int(resultado, 2)
        
        # Para suma y resta (aunque este caso no debería ocurrir)
        return a * b if operador == '*' else a / b
    
    def calcular_operacion(self):
        try:
            expresion_original = self.entry.get().replace(" ", "")
            
            if not re.match(r'^[\d.,+\-*/]+$', expresion_original):
                raise ValueError("Formato inválido. Use solo números y operadores básicos.")
            
            expresion = expresion_original.replace(",", ".")
            
            # Primero manejar multiplicaciones y divisiones, incluyendo signos negativos
            while re.search(r'([\d.]+|-\d+\.?\d*)([*/])(-?[\d.]+)', expresion):
                match = re.search(r'([\d.]+|-\d+\.?\d*)([*/])(-?[\d.]+)', expresion)
                if match:
                    numero1, operador, numero2 = match.groups()
                    
                    # Determinar si es operación entera o flotante
                    es_entero = (not self.es_decimal(numero1) and not self.es_decimal(numero2))
                    
                    if es_entero:
                        # Convertir a enteros (manejar signos)
                        num1 = int(float(numero1))
                        num2 = int(float(numero2))
                        
                        enteros = OperarEnteros([abs(num1), abs(num2)])
                        if operador == '*':
                            resultado = enteros.operar_todos('multiplicacion')
                            res = int(resultado, 2)
                        elif operador == '/':
                            resultado = enteros.operar_todos('division')
                            res = int(resultado, 2)
                        
                        # Aplicar signo
                        signo = -1 if (num1 < 0) ^ (num2 < 0) else 1
                        res *= signo
                    else:
                        # Operación flotante
                        num1 = float(numero1)
                        num2 = float(numero2)
                        
                        flotantes = OperarFlotantes([abs(num1), abs(num2)])
                        if operador == '*':
                            resultado = flotantes.operar_todos('multiplicacion')
                            res = float(flotantes.formatear_flotante(resultado))
                        elif operador == '/':
                            resultado = flotantes.operar_todos('division')
                            res = float(flotantes.formatear_flotante(resultado))
                        
                        # Aplicar signo
                        signo = -1 if (num1 < 0) ^ (num2 < 0) else 1
                        res *= signo
                    
                    expresion = expresion.replace(match.group(0), str(res))
            
            # Ahora resolver sumas y restas
            resultado = eval(expresion)
            
            # Convertir a binario según el tipo de resultado
            if isinstance(resultado, int) or (isinstance(resultado, float) and resultado.is_integer()):
                resultado_entero = int(resultado)
                resultado_binario = self.entero_operador.convertir_a_binario(resultado_entero)
            else:
                resultado_binario = self.flotante_operador.formatear_binario(
                    self.flotante_operador.convertir_a_binario(resultado)
                )
            
            self.label_resultado.config(text=f"Resultado: {resultado}")
            self.label_binario.config(text=f"Binario: {resultado_binario}")
        
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()