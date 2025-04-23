from random import randrange
print("CALCULADORA CONJUNTOS TALLER JOSE")
cant1 = int(input("Digite la cardinalidad del conjunto A: "))
cant2 = int(input("Digite la cardinalidad del conjunto B: "))
conjunto1 = set()
conjunto2 = set()

while len(conjunto1) < cant1:
    conjunto1.add(randrange(0,30))

while len(conjunto2) < cant2:
    conjunto2.add(randrange(0,30))

union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
diferencia = conjunto1.difference(conjunto2)
diferenciaSimetrica = conjunto1.symmetric_difference(conjunto2)

print("El conjunto A es: ", conjunto1)
print("El conjunto B es: ", conjunto2)
print("La Unión (∪): A ∪ B es: ", union)
print("La Intersección (∩): A ∩ B es: ", interseccion)
print("La diferencia (−): A − B es: ", diferencia)
print("La diferencia simétrica (Δ): A Δ B es: ", diferenciaSimetrica)

