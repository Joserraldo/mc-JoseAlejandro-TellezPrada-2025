import math 
'''1) Ayer dejé mi teléfono celular olvidado en el autobús, por lo que lo reemplacé
rápidamente por un teléfono con menor capacidad de memoria. En mi
teléfono anterior tenía instaladas 20 aplicaciones y ahora solamente puedo
seleccionar 8.
a) ¿De cuántas formas puedo realizar esta selección?
b) Si deseo mantener instaladas 3 de las 6 aplicaciones de redes sociales que tenía
y otras 5 aplicaciones de las 14 restantes, ¿de cuántas formas puedo
seleccionar ahora?'''
print("Vamos a hacer combinacion pues el orden de las aplicaciones no importa")
print(f"a) C(8,5) = {math.factorial(8)/(math.factorial(5)*math.factorial(8-5))}") 
print(f"b) C(6,3)*C(14,5) = {math.factorial (6)/(math.factorial(3)*math.factorial(6-3))} * { math.factorial(14)/(math.factorial(5)*math.factorial(14-5)) } = {(math.factorial (6)/(math.factorial(3)*math.factorial(6-3))) *  (math.factorial(14)/(math.factorial(5)*math.factorial(14-5))) }")



'''Una baraja común de 52 cartas consiste en cuatro palos (tréboles, diamantes,
corazones y espadas) con 13 denominaciones cada uno (as, de 2 a 10, jack [J],
reina [Q] y rey [K]).
a) ¿Cuántas manos de póquer (sin ordenar) de cinco cartas, seleccionadas de una
baraja común de 52 cartas, existen?
b) ¿Cuántas manos de póquer contienen cartas todas del mismo palo?
c) ¿Cuántas manos de póquer contienen tres cartas de una denominación y dos
de una segunda denominación?'''
print("Vamos a hacer combinacion pues el orden de las cartas no importa")
print(f"a) C(52,5) = {math.factorial(52)/(math.factorial(5)*math.factorial(52-5))}")
print(f"b) 4*C(13,5) = {4*(math.factorial(13)/(math .factorial(5)*math.factorial(13-5)))}")
print(f"c) 13*C(4,3)*12*C(4,2) = 13{(math.factorial(4)/(math.factorial(3)*math.factorial(4-3)))} * 12{ (math.factorial(4)/(math.factorial(2)*math.factorial(4-2 ))) } = {13*(math.factorial(4)/(math.factorial(3)*math.factorial( 4-3))) *  12*(math.factorial(4)/(math.factorial(2)*math.factorial(4-2))) }")
