import math
input("-----[TALLER JOSE]-----\npresiona [ENTER] para continuar...")
'''La fábrica de automóviles Summer fabrica su popular modelo
Sunshine en 3 colores, 5 líneas, 3 tipos de transmisión y 2 cilindrajes
diferentes.
a) ¿Cuántos tipos diferentes de vehículos se pueden fabricar?
b) Si ahora se ofrecen en 10 colores diferentes, ¿cuántos tipos se tendrán ahora?'''
print("FABRICA AUTOMOVILES SUNSHINE")
print("a) ¿Cuántos tipos diferentes de vehículos se pueden fabricar?")
print("La respuesta es: 3*5*3*2 =", 3*5*3*2)
print("b) Si ahora se ofrecen en 10 colores diferentes, ¿cuántos tipos se tendrán ahora?")
print("La respuesta es: 10*5*3*2 =", 10*5*3*2)

'''Las placas de automóviles en Colombia contienen 3 letras seguidas de
tres números. Entre las letras no se incluye la Ñ.
a) ¿Cuántas placas de automóvil diferentes existen?
b) ¿Cuántas se podrían hacer si no se aceptan repeticiones de letras o
números?'''
print("PLACAS DE AUTOMOVIL COLOMBIA")
print("a) ¿Cuántas placas de automóvil diferentes existen?")
print("La respuesta es: 26^3*10^3 =", 26**3*10**3)
print("b) ¿Cuántas se podrían hacer si no se aceptan repeticiones de letras o números?")
print("La respuesta es: 26*25*24*10*9*8 =", 26*25*24*10*9*8)


'''¿De cuántas maneras se puede seleccionar el presidente,
vicepresidente, secretario y tesorero de un grupo de 10 personas?'''
print("SELECCION DE PERSONAS")
print("La respuesta es: 10*9*8*7 =", 10*9* 8*7)

'''¿Cuántas cadenas de 16 bits comienzan y terminan con números
00? Ejemplos: 0010110000101100, 0001010000010100,
0011000000110000'''
print("CADENAS DE 16 BITS")
print("La respuesta es: 2^12 =", 2**12)

'''Un coleccionista de libros antiguos desea ubicar sus 9 libros más
preciados en una vitrina antirrobos, uno al lado del otro. 4 de los
libros están escritos en griego y los 5 restantes en latín. Cada uno
de los libros es diferente de los demás.
a) ¿De cuántas formas se pueden ubicar los libros en la vitrina?
b) ¿De cuantas formas se pueden ubicar si todos los libros en latín
deben estar uno al lado del otro?
c) Si desea alternar los libros (latín, griego, latín, griego, etc.), ¿de
cuántas formas se pueden ubicar ahora?'''
print("COLECCION DE LIBROS ANTIUOS")
print("a) ¿De cuántas formas se pueden ubicar los libros en la vitrina ?")
print("La respuesta es: 9! =", math.factorial(9))
print("b) ¿De cuantas formas se pueden ubicar si todos los libros en latín deben estar uno al lado del otro?")
print("La respuesta es: 5! x 4! =", math.factorial(5)*math.factorial(4))
print("c) Si desea alternar los libros (latín, griego, latín, griego, etc.), ¿de cuántas formas se pueden ubicar ahora?")
print("La respuesta es: 2*(5! x 4!) =", 2*(math.factorial(5)*math.factorial(4)))
