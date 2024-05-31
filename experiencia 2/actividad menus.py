cupo = 100000
op = 0
compra = 0


while op != 3:
    #manejando error de numero en input de int
    try:
        #se da la bienvenida y se empieza el menú, pidiendo la opción del usuario
        print("Te damos la bienvenida al menú de tu tarjeta, elige una de las siguientes opciones: \n 1. Pago tarjeta de crédito. \n 2. Simulación de compras. \n 3. Salir.")
        op = int(input("Ingrese la opción deseada: "))
        if op != 1 and op != 2 and op != 3: #comprobando que el op dado sea una de las opciones
            print("Por favor ingrese una de las opciones mostradas. (1, 2 o 3 para salir) ")
        elif op == 1:
            try:
                print("Usted ha elegido la opción para pagar su tarjeta de crédito, su deuda es de -$100.000")
                pago = int(input("Ingrese el monto a pagar, este no puede exceder el monto actual de la tarjeta: "))
                if pago > 0 or pago < cupo:
                    cupo = cupo - pago
                    print(f"Usted ha hecho el pago con éxito, su cupo es de: {cupo}")
                else:
                    print("Su pago debe ser mayor a 0 y menor a su saldo actual")
            except ValueError:
                print("Debe ingresal el monto en forma de dígito. ")
        elif op == 2:
            try:
                print("Usted ha elegido la opción para simular sus compras")
                veces = int(input("Ingrese el número de compras a simular:"))
                for i in range(veces):
                    valor = int(input("Ingrese el valor de esta compra simulada: "))
                    compra = valor + compra
                    cupo = cupo + compra
                    print(f"Su saldo quedaría en {cupo}")
            except ValueError:
                print("Ingrese el número de comoras en formato numérico")
        elif op == 3:
                  print("Adiós")
    except ValueError:
        print("Debe ingresal el monto en forma de dígito.")

        
    
        







    """except  ValueError:
     print("Debe ingresal el número de la opción elegida en forma de dígito.")"""