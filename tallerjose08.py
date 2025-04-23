def decimal_a_hexadecimal(numero):
    if numero == 0:
        return "0"
    
    # Dígitos hexadecimales
    digitos_hex = "0123456789ABCDEF"
    resultado = ""
    
    # Número negativo
    es_negativo = False
    if numero < 0:
        es_negativo = True
        numero = abs(numero)
    
    # Proceso de divisiones sucesivas
    while numero > 0:
        residuo = numero % 16
        resultado = digitos_hex[residuo] + resultado
        numero //= 16
    
    if es_negativo:
        resultado = "-" + resultado
        
    return resultado

def octal_a_decimal(numero_str):

    # Verificar si es un número válido en base 8
    if not all(digito in '01234567' for digito in numero_str.replace('-', '', 1)):
        return None
    
    # Manejar números negativos
    es_negativo = False
    if numero_str.startswith('-'):
        es_negativo = True
        numero_str = numero_str[1:]
    
    resultado = 0
    potencia = 0
    
    # Proceso de potencias sucesivas (de derecha a izquierda)
    for digito in reversed(numero_str):
        resultado += int(digito) * (8 ** potencia)
        potencia += 1
    
    if es_negativo:
        resultado = -resultado
        
    return resultado

def menu_principal():
    """
    Función principal que muestra un menú y ejecuta las conversiones.
    """
    while True:
        print("\n===[CONVERSOR DE BASES NUMÉRICAS]===")
        print("1. Convertir de decimal (base 10) a hexadecimal (base 16)")
        print("2. Convertir de octal (base 8) a decimal (base 10)")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1-3): ")
        
        if opcion == '1':
            try:
                numero = int(input("Ingrese un número en base 10: "))
                resultado = decimal_a_hexadecimal(numero)
                print(f"El número {numero} en hexadecimal es: {resultado}")
                input("Presione [ENTER] para continuar...")
            except ValueError:
                print("Error: Por favor ingrese un número entero válido.")
                input("Presione [ENTER] para continuar...")
                
        elif opcion == '2':
            numero_str = input("Ingrese un número en base 8: ")
            resultado = octal_a_decimal(numero_str)
            input("Presione [ENTER] para continuar...")
            
            if resultado is None:
                print("Error: El número ingresado no es válido en base 8.")
                input("Presione [ENTER] para continuar...")
            else:
                print(f"El número {numero_str} en base 10 es: {resultado}")
                input("Presione [ENTER] para continuar...")
                
        elif opcion == '3':
            print("¡Gracias por usar el conversor de bases numéricas!\nPowered by ing. José A. Téllez P.\nDonaciones nequi: 3115349124") 
            break
            
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            input("Presione [ENTER] para continuar...")


menu_principal()
