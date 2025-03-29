class OperarEnteros:
    def __init__(self, numeros=None, bits=32):
        # Inicializamos con una lista vacía si no se proporciona
        self.numeros = numeros if numeros is not None else []
        self.bits = bits
        
    def agregar_numero(self, numero):
        # Método para agregar un número a la lista
        self.numeros.append(numero)
        
    def convertir_a_binario(self, n=None):
        # Si no se proporciona un número, convertimos todos los de la lista
        if n is None:
            return [self._convertir_numero(num) for num in self.numeros]
        else:
            # Si se proporciona un número, convertimos solo ese
            return self._convertir_numero(n)
    
    def _convertir_numero(self, n):
        # Método auxiliar para convertir un número individual
        if n >= 0: 
            binario = bin(n)[2:].zfill(self.bits)
        else:
            # Para negativos, usamos complemento a 2
            binario_abs = bin(abs(n))[2:].zfill(self.bits)
            binario_inv = ''.join('1' if bit == '0' else '0' for bit in binario_abs)
        
            valor_decimal = int(binario_inv, 2) + 1
            binario = bin(valor_decimal)[2:].zfill(self.bits)

            if len(binario) > self.bits:
                binario = binario[-self.bits:]

        return binario
    
    def _operar_binario(self, bin1, bin2, operacion):
        # Método para realizar cualquier operación entre dos números binarios
        num1 = int(bin1, 2)
        num2 = int(bin2, 2)
        
        if operacion == 'suma':
            resultado = num1 + num2
        elif operacion == 'resta':
            resultado = num1 - num2
        elif operacion == 'multiplicacion':
            resultado = num1 * num2
        elif operacion == 'division':
            if num2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            resultado = num1 // num2  # División entera
        else:
            raise ValueError(f"Operación '{operacion}' no soportada")
        
        # Convertir el resultado a binario
        if resultado >= 0:
            resultado_bin = bin(resultado)[2:].zfill(self.bits)
        else:
            # Para resultados negativos, usamos el mismo proceso de complemento a 2
            resultado_abs = abs(resultado)
            binario_abs = bin(resultado_abs)[2:].zfill(self.bits)
            binario_inv = ''.join('1' if bit == '0' else '0' for bit in binario_abs)
            
            valor_decimal = int(binario_inv, 2) + 1
            resultado_bin = bin(valor_decimal)[2:].zfill(self.bits)
        
        # Truncar si es necesario
        if len(resultado_bin) > self.bits:
            resultado_bin = resultado_bin[-self.bits:]
            
        return resultado_bin
    
    def suma_binario(self, bin1, bin2):
        return self._operar_binario(bin1, bin2, 'suma')
    
    def resta_binario(self, bin1, bin2):
        return self._operar_binario(bin1, bin2, 'resta')
    
    def multiplicacion_binario(self, bin1, bin2):
        return self._operar_binario(bin1, bin2, 'multiplicacion')
    
    def division_binario(self, bin1, bin2):
        return self._operar_binario(bin1, bin2, 'division')
    
    def operar_todos(self, operacion='suma'):
        # Realiza la operación indicada entre todos los números de la lista
        if not self.numeros:
            return "No hay números para operar"
        
        numeros_binarios = self.convertir_a_binario()  # Convertimos todos
        resultado = numeros_binarios[0]
        
        for i in range(1, len(numeros_binarios)):
            if operacion == 'suma':
                resultado = self.suma_binario(resultado, numeros_binarios[i])
            elif operacion == 'resta':
                resultado = self.resta_binario(resultado, numeros_binarios[i])
            elif operacion == 'multiplicacion':
                resultado = self.multiplicacion_binario(resultado, numeros_binarios[i])
            elif operacion == 'division':
                resultado = self.division_binario(resultado, numeros_binarios[i])
            else:
                raise ValueError(f"Operación '{operacion}' no soportada")
            
        return resultado

'''# Ejemplo de uso:
entero = OperarEnteros([10, 20, 30, -5])

# Convertir todos a binario
binarios = entero.convertir_a_binario()
print("Números en binario:", binarios)

# Realizar diferentes operaciones con todos los números
suma = entero.operar_todos('suma')
print("Suma en binario:", suma)
print("Suma en decimal:", int(suma, 2) if suma != "No hay números para operar" else suma)

resta = entero.operar_todos('resta')
print("Resta en binario:", resta)
print("Resta en decimal:", int(resta, 2) if resta != "No hay números para operar" else resta)

multiplicacion = entero.operar_todos('multiplicacion')
print("Multiplicación en binario:", multiplicacion)
print("Multiplicación en decimal:", int(multiplicacion, 2) if multiplicacion != "No hay números para operar" else multiplicacion)

# Crear nueva instancia para probar división
divisor = OperarEnteros([100, 5, 2])
division = divisor.operar_todos('division')
print("División en binario:", division)
print("División en decimal:", int(division, 2) if division != "No hay números para operar" else division)'''
