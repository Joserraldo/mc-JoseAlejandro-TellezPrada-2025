while True:
    print("CALCULADORA CONJUNTOS TALLER JOSE")
    try:
        cant1 = int(input("Digite la cardinalidad del conjunto universal U: "))
        cant2 = int(input("Digite la cardinalidad del subconjunto A: "))
    
        if cant1 > cant2 and cant1>=0 and cant2>=0 : 
            conjunto1 = set()
            conjunto2 = set()

            while len(conjunto1) < cant1:
                conjunto1.add( int(input(f"Escriba los elementos para su conjunto U , cantidad restante {cant1-len(conjunto1)}: ")))

            while len(conjunto2) < cant2:
                conjunto2.add( int(input(f"Escriba los elementos para su subconjunto A , cantidad restante {cant2-len(conjunto2) }: ")))


            if conjunto1.union(conjunto2) == conjunto1:
                op1=(conjunto1.intersection(conjunto2)).union(conjunto2) #A
                op2= (conjunto1.difference(conjunto2)).intersection(conjunto2) #vacio
                op3= (conjunto1.difference(conjunto2)).difference(conjunto2) #complemento de A

                print("El conjunto universal U es: ", conjunto1)
                print("El subconjunto A es: ", conjunto2)
                print("La operación (U⋂A)⋃A es: ", op1)
                print("La operación (U − A) ⋂ A es: ", op2)
                print("La operación (U⨁A) − A es: ", op3)
                break
            else:
                input("vuelva a dijitar los datos debido a que los conjuntos universal (U) y subconjunto (A) no concuerdan o no estan bien distribuidos\npresiona enter para continuar...")
        else:
            input("Error: La cardinalidad del subconjunto A no puede ser mayor a la cardinalidad del conjunto universal U ni tampoco puede tomar valores negativos, vuelva a digitar los valores\npresiona enter para continuar...")
    except ValueError: 
     print("ingrese un numero valido")
