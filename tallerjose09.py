def convertir(numero):
    """
    - 1 dígito para el signo
    - 4 dígitos para el exponente con signo
    - 7 dígitos para la mantisa (0.ddddddd)
    """
    signo = 0 if numero >= 0 else 1
    numero = abs(numero)
    
    if numero == 0:
        exponente = 0
        mantisa = 0
    else:
        exponente = 0
        while numero >= 1:
            numero /= 10
            exponente += 1
        
        while numero < 0.1 and numero > 0:
            numero *= 10
            exponente -= 1
        
        mantisa = numero
    
    return signo, exponente, mantisa

def flotante(signo, exponente, mantisa):
    # Signo: + o -
    signo_str = "-" if signo == 1 else "+"
    
    # Exponente: +XXXX o -XXXX (4 espacios)
    exponente_signo = "-" if exponente < 0 else "+"
    exponente_str = f"{abs(exponente):04d}"
    
    # Mantisa: 7 dígitos (sin el punto decimal)
    # Convertir a cadena y tomar los 7 primeros dígitos significativos
    mantisa_str = f"{mantisa:.7f}".replace("0.", "")[:7].ljust(7, '0')
    
    return f"({signo_str}, {exponente_signo}{exponente_str}, {mantisa_str})"

def formato_cientifico(signo, exponente, mantisa):

    exp_cientifico = exponente
    
    if signo == 1:
        return f"-{mantisa:.6f} × 10^{exp_cientifico}"
    else:
        return f"{mantisa:.6f} × 10^{exp_cientifico}"

def convertir_a_float(numero_str):
    """Convierte una cadena con formato de número español a float :D"""
    # Primero remover puntos de miles (asumiendo formato español)
    sin_miles = numero_str.replace('.', '')

    return float(sin_miles.replace(',', '.'))

def suma_punto_flotante(num1, num2):

    num1 = convertir_a_float(num1)
    num2 = convertir_a_float(num2)

    resultado = num1 + num2

    signo, exponente, mantisa = convertir(resultado)

    return flotante(signo, exponente, mantisa), formato_cientifico(signo, exponente, mantisa)

def resta_punto_flotante(num1, num2):

    num1 = convertir_a_float(num1)
    num2 = convertir_a_float(num2)

    resultado = num1 - num2

    signo, exponente, mantisa = convertir(resultado)

    return flotante(signo, exponente, mantisa), formato_cientifico(signo, exponente, mantisa)

def multiplicacion_punto_flotante(num1, num2):

    num1 = convertir_a_float(num1)
    num2 = convertir_a_float(num2)

    resultado = num1 * num2

    signo, exponente, mantisa = convertir(resultado)
    
    return flotante(signo, exponente, mantisa), formato_cientifico(signo, exponente, mantisa)

def division_punto_flotante(num1, num2):

    num1 = convertir_a_float(num1)
    num2 = convertir_a_float(num2)
    
    resultado = num1 / num2
    
    signo, exponente, mantisa = convertir(resultado)
    
    return flotante(signo, exponente, mantisa), formato_cientifico(signo, exponente, mantisa)

# tabla con los resultados
print("|------------------------|---------------------|-----------------------------------|")
print("|       Operación        |  Notación flotante  | Equivalente en notación científica|")
print("|------------------------|   (S,EEEE,MMMMMMM)  |-----------------------------------|")
print("|------------------------|---------------------|-----------------------------------|")

# a) 68.327,54 + 0,007988
num1a = "68.327,54"
num2a = "0,007988"
resultado_a, cientifico_a = suma_punto_flotante(num1a, num2a)
print(f"|  {num1a} + {num2a}  | {resultado_a} |           {cientifico_a}         |")

# b) 748,067 - 41.322,006
num1b = "748,067"
num2b = "41.322,006"
resultado_b, cientifico_b = resta_punto_flotante(num1b, num2b)
print(f"|  {num1b} - {num2b}  | {resultado_b} |          {cientifico_b}         |")

# c) 0,40172 * 0,00011109
num1c = "0,40172"
num2c = "0,00011109"
resultado_c, cientifico_c = multiplicacion_punto_flotante(num1c, num2c)
print(f"|  {num1c} * {num2c}  | {resultado_c} |           {cientifico_c}        |")

# d) 29,95091 / 0,000110793
num1d = "29,95091"
num2d = "0,000110793"
resultado_d, cientifico_d = division_punto_flotante(num1d, num2d)
print(f"| {num1d} / {num2d} | {resultado_d} |           {cientifico_d}         |")
print("|------------------------|---------------------|-----------------------------------|")
print("Agradecimiento especial a la ia... la verdad pense que si podia hacerlo en clase pero estaba mas complicado \nde lo que pense, y el ciclo para los numeros que estaban mayores al 0,... \ntocaba era >=1 no >= 0, por eso es que en la clase no me servia porque con >= 0 pues es un bucle infinito asi \nlo divida todo el tiempo nunca va a dejar de ser mayor a 0 , igual aprendi bastante de como mover \nStrings entonces epico :D ")
