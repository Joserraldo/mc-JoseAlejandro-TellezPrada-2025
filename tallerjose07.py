'''voy a usar strings porque es mucho mas facil que listas, aunque un string es una lista 
de caracteres, es mas comodo :) '''
def convertir_a_binario(n, bits=16):

    if n >= 0: 
        binario = bin(n)[2:].zfill(bits)

    else:
        binario_positivo = bin(abs(n))[2:].zfill(bits)
        binario_invertido = ''.join('1' if bit == '0' else '0' for bit in binario_positivo)

        valor_decimal = int(binario_invertido, 2) + 1
        binario = bin(valor_decimal)[2:].zfill(bits)
      
        if len(binario) > bits:
            binario = binario[-bits:]
            
    return binario

def binario_a_decimal(binario):
 
    if binario[0] == '0':
        return int(binario, 2)
    else:  
        
        binario_invertido = ''.join('1' if bit == '0' else '0' for bit in binario)
        
        return -(int(binario_invertido, 2) + 1)

def suma_binaria(bin1, bin2):

    decimal1 = binario_a_decimal(bin1)
    decimal2 = binario_a_decimal(bin2)
    suma_decimal = decimal1 + decimal2
    
    return convertir_a_binario(suma_decimal)

print("---[CALCULADORA SUMA BINARIOS]---")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

binario1 = convertir_a_binario(num1)
binario2 = convertir_a_binario(num2)

resultado_binario = suma_binaria(binario1, binario2)

resultado_decimal = binario_a_decimal(resultado_binario)

print(f"Primer número en binario : {binario1}")
print(f"Segundo número en binario: {binario2}")
print(f"Resultado en binario     : {resultado_binario}")
print(f"Resultado en decimal     : {resultado_decimal}")
