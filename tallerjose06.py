import math 
print("Programa de aproximación del coseno")
print("-------------------------------")
while True:
    try:
        x = float(input("Ingrese el valor de x en radianes: "))
        erros_esperado = 0.5*(10**-8)*100
        error_aprox = 100
        iteracion = 0
        potencia = 0
        valor = 0
        anterior = 0
        while error_aprox >erros_esperado:
            if iteracion%2 == 0:
                anterior = valor
                valor += (x**potencia /math.factorial(potencia))
                potencia +=2
                error_aprox = (abs(valor -anterior)/valor)*100
                iteracion +=1
            else:
                anterior = valor
                valor -= (x**potencia /math.factorial(potencia))
                potencia +=2
                error_aprox = (abs(valor -anterior)/valor)*100
                iteracion +=1
        print(f"El valor aproximado del coseno de {x} es: {valor}  y se tuvieron que hacer {iteracion} iteraciones, con un error de {error_aprox}%, lo cual resulta menor que el error esperado de {erros_esperado}% ")
    except ValueError:
        print("Error: Ingrese un valor numérico")
