from itertools import product

# Definir los valores de verdad
conjunto_s = [True, False]

print("-" * 15 + "[Tablas Algebra Booleana]" + "-" * 15)
input(f'Presiona "ENTER" para ver el taller de Jose...')

# a) Leyes asociativas
print("\na) Leyes asociativas:")
print(f"\n{'X':<5}{'Y':<5}{'Z':<5}{'(X ∨ Y) ∨ Z':<15}{'X ∨ (Y ∨ Z)':<20}")
print("=" * 55)

for x, y, z in product(conjunto_s, repeat=3):
    col1 = (x or y) or z
    col2 = x or (y or z)
    print(f"{x:<5}{y:<5}{z:<5}{col1:<15}{col2:<20}")

print(f"\n{'X':<5}{'Y':<5}{'Z':<5}{'(X ∧ Y) ∧ Z':<15}{'X ∧ (Y ∧ Z)':<20}")
print("=" * 55)

for x, y, z in product(conjunto_s, repeat=3):
    col1 = (x and y) and z
    col2 = x and (y and z)
    print(f"{x:<5}{y:<5}{z:<5}{col1:<15}{col2:<20}")

# b) Leyes conmutativas
print("\nb) Leyes conmutativas:")

print(f"\n{'X':<5}{'Y':<5}{'X ∨ Y':<15}{'Y ∨ X':<20}")
print("=" * 55)

for x, y in product(conjunto_s, repeat=2):
    col1 = x or y
    col2 = y or x
    print(f"{x:<5}{y:<5}{col1:<15}{col2:<20}")

print(f"\n{'X':<5}{'Y':<5}{'X ∧ Y':<15}{'Y ∧ X':<20}")
print("=" * 55)

for x, y in product(conjunto_s, repeat=2):
    col1 = x and y
    col2 = y and x
    print(f"{x:<5}{y:<5}{col1:<15}{col2:<20}")

# c) Leyes distributivas
print("\nc) Leyes distributivas:")
print(f"\n{'X':<5}{'Y':<5}{'Z':<5}{'X ∧ (Y ∨ Z)':<15}{'(X ∧ Y) ∨ (X ∧ Z)':<20}")
print("=" * 55)

for x, y, z in product(conjunto_s, repeat=3):
    col1 = x and (y or z)
    col2 = (x and y) or (x and z)
    print(f"{x:<5}{y:<5}{z:<5}{col1:<15}{col2:<20}")

print(f"\n{'X':<5}{'Y':<5}{'Z':<5}{'X ∨ (Y ∧ Z)':<15}{'(X ∨ Y) ∧ (X ∨ Z)':<20}")
print("=" * 55)

for x, y, z in product(conjunto_s, repeat=3):
    col1 = x or (y and z)
    col2 = (x or y) and (x or z)
    print(f"{x:<5}{y:<5}{z:<5}{col1:<15}{col2:<20}")

# d) Leyes de identidad
print("\nd) Leyes de identidad:")
print(f"\n{'X':<5}{'X ∧ 0 (False)':<15}{'0 (False)':<10}")
print("=" * 40)

for x in conjunto_s:
    col1 = x and False
    col2 = False
    print(f"{x:<5}{col1:<15}{col2:<10}")

print(f"\n{'X':<5}{'X ∨ 1 (True)':<15}{'1 (True)':<10}")
print("=" * 40)

for x in conjunto_s:
    col1 = x or True
    col2 = True
    print(f"{x:<5}{col1:<15}{col2:<10}")

# e) Leyes de complemento
print("\ne) Leyes de complemento:")
print(f"\n{'X':<5}{'X´':<5}{'X ∨ X´':<15}{'1':<10}")
print("=" * 40)

for x in conjunto_s:
    x_prima = not x
    col1 = x or x_prima
    print(f"{x:<5}{x_prima:<5}{col1:<15}{1:<10}")

print(f"\n{'X':<5}{'X´':<5}{'X ∧ X´':<15}{'0':<10}")
print("=" * 40)

for x in conjunto_s:
    x_prima = not x
    col1 = x and x_prima
    print(f"{x:<5}{x_prima:<5}{col1:<15}{0:<10}")
