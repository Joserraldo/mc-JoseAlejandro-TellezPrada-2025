class OperarFlotantes:
    def __init__(self, numeros=None, bits_mantisa=23, bits_exponente=8, bits_signo=1):
        # Inicializamos con una lista vacía si no se proporciona
        self.numeros = numeros if numeros is not None else []
        self.bits_mantisa = bits_mantisa
        self.bits_exponente = bits_exponente
        self.bits_signo = bits_signo
        
    def agregar_numero(self, numero):
        # Método para agregar un número a la lista
        self.numeros.append(numero)
        
    def _float_a_binario(self, numero):
        # Convertir un número flotante a su representación binaria (signo, exponente, mantisa)
        # Obtener el signo
        signo = 1 if numero < 0 else 0
        numero = abs(numero)
        
        if numero == 0:
            # Caso especial: cero
            exponente_bin = '0' * self.bits_exponente
            mantisa_bin = '0' * self.bits_mantisa
        else:
            # Convertir a binario
            # Encontrar el exponente que normaliza el número (1.xxxxx * 2^exp)
            exponente = 0
            temp = numero
            
            # Si número >= 2, dividimos hasta que sea 1.xxx
            while temp >= 2:
                temp /= 2
                exponente += 1
                
            # Si número < 1, multiplicamos hasta que sea 1.xxx
            while temp < 1 and temp > 0:
                temp *= 2
                exponente -= 1
            
            # Calcular el exponente con sesgo (bias)
            # Formato IEEE 754 para números de simple precisión (32 bits) usa sesgo de 127
            bias = (2 ** (self.bits_exponente - 1)) - 1
            exponente_sesgado = exponente + bias
            
            # Verificar overflow/underflow del exponente
            if exponente_sesgado < 0:
                exponente_sesgado = 0  # Subdesbordamiento (underflow)
                temp = 0  # Mantisa será cero
            elif exponente_sesgado >= (2 ** self.bits_exponente) - 1:
                exponente_sesgado = (2 ** self.bits_exponente) - 1  # Desbordamiento (overflow)
                temp = 0  # Mantisa será cero
                
            # Convertir exponente a binario
            exponente_bin = bin(exponente_sesgado)[2:].zfill(self.bits_exponente)
            
            # Calcular la mantisa (parte fraccionaria de la representación normalizada)
            # Parte fraccional después de normalizar (1.xxxx -> solo almacenamos xxxx)
            mantisa = temp - 1.0  # Quitar el 1 implícito
            mantisa_bin = ''
            
            # Convertir la parte fraccional a binario
            for _ in range(self.bits_mantisa):
                mantisa *= 2
                bit = int(mantisa)
                mantisa_bin += str(bit)
                mantisa -= bit
                
        return signo, exponente_bin, mantisa_bin
    
    def _binario_a_float(self, signo, exponente_bin, mantisa_bin):
        # Convertir de representación binaria a número flotante
        
        if exponente_bin == '0' * self.bits_exponente and mantisa_bin == '0' * self.bits_mantisa:
            # Caso especial: cero
            return 0.0
            
        # Convertir exponente a decimal
        exponente_decimal = int(exponente_bin, 2)
        
        # Aplicar el sesgo para obtener el exponente real
        bias = (2 ** (self.bits_exponente - 1)) - 1
        exponente_real = exponente_decimal - bias
        
        # Convertir mantisa
        mantisa_decimal = 0
        for i, bit in enumerate(mantisa_bin):
            if bit == '1':
                mantisa_decimal += 2 ** -(i + 1)
                
        # Valor final = (-1)^signo * (1 + mantisa) * 2^exponente
        valor = (1 + mantisa_decimal) * (2 ** exponente_real)
        
        # Aplicar el signo
        if signo == 1:
            valor = -valor
            
        return valor
    
    def convertir_a_binario(self, n=None):
        # Si no se proporciona un número, convertimos todos los de la lista
        if n is None:
            return [self._float_a_binario(num) for num in self.numeros]
        else:
            # Si se proporciona un número, convertimos solo ese
            return self._float_a_binario(n)
    
    def _operar_binario(self, bin_rep1, bin_rep2, operacion):
        # Convertir las representaciones binarias a flotantes
        float1 = self._binario_a_float(*bin_rep1)
        float2 = self._binario_a_float(*bin_rep2)
        
        # Realizar la operación
        if operacion == 'suma':
            resultado = float1 + float2
        elif operacion == 'resta':
            resultado = float1 - float2
        elif operacion == 'multiplicacion':
            resultado = float1 * float2
        elif operacion == 'division':
            if float2 == 0:
                raise ZeroDivisionError("No se puede dividir por cero")
            resultado = float1 / float2
        else:
            raise ValueError(f"Operación '{operacion}' no soportada")
        
        # Convertir el resultado a la representación binaria
        return self._float_a_binario(resultado)
    
    def suma_binario(self, bin_rep1, bin_rep2):
        return self._operar_binario(bin_rep1, bin_rep2, 'suma')
    
    def resta_binario(self, bin_rep1, bin_rep2):
        return self._operar_binario(bin_rep1, bin_rep2, 'resta')
    
    def multiplicacion_binario(self, bin_rep1, bin_rep2):
        return self._operar_binario(bin_rep1, bin_rep2, 'multiplicacion')
    
    def division_binario(self, bin_rep1, bin_rep2):
        return self._operar_binario(bin_rep1, bin_rep2, 'division')
    
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
    
    def formatear_binario(self, bin_rep):
        # Formatea la representación binaria para visualización
        signo, exponente_bin, mantisa_bin = bin_rep
        
        signo_str = "1" if signo == 1 else "0"
        
        return f"{signo_str} | {exponente_bin} | {mantisa_bin}"
    
    def formatear_flotante(self, bin_rep):
        # Formatea el valor flotante para visualización
        valor = self._binario_a_float(*bin_rep)
        return f"{valor}"

'''# Ejemplo de uso:
flotantes = OperarFlotantes([3.14, 2.71, -1.618,30])

# Convertir todos a binario
binarios = flotantes.convertir_a_binario()
print("Números en binario (signo | exponente | mantisa):")
for i, bin_rep in enumerate(binarios):
    print(f"{flotantes.numeros[i]} -> {flotantes.formatear_binario(bin_rep)}")

# Realizar operaciones
print("\nOperaciones:")
suma = flotantes.operar_todos('suma')
print(f"Suma en binario: {flotantes.formatear_binario(suma)}")
print(f"Suma en decimal: {flotantes.formatear_flotante(suma)}")

resta = flotantes.operar_todos('resta')
print(f"Resta en binario: {flotantes.formatear_binario(resta)}")
print(f"Resta en decimal: {flotantes.formatear_flotante(resta)}")

multiplicacion = flotantes.operar_todos('multiplicacion')
print(f"Multiplicación en binario: {flotantes.formatear_binario(multiplicacion)}")
print(f"Multiplicación en decimal: {flotantes.formatear_flotante(multiplicacion)}")

division = flotantes.operar_todos('division')
print(f"División en binario: {flotantes.formatear_binario(division)}")
print(f"División en decimal: {flotantes.formatear_flotante(division)}")'''