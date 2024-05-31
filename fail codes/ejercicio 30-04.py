#menú verdulería
#papas a 2000
#naranjas a 1000 limon a 1000

op = int(input("Te damos la bienvenida a nuestra tienda, elige una opción. \n 1. COmprar \n 2. Pagar \n 3. Salir "))
compra = 0
papas = 2000
limon = 1000
naranjas = 1000

while op != 3:
    try:
        if op != 1 or op != 2 or op !=3:
            op = int(input("Eliga una opcion del 1 al 3: 1"))
        else :
            if op == 1: # opC es para opcion de compra
              opC = input("Ingrese que desea comprar \n Papas 3 kilos a $2000 \n Kilo de naranjas a $1000 \n Kilo de limones a $1000")<<<<
              opC = (opC.lower)
                    if opC != "papas" and opC != "narnajas" and opC != "limon" and opC != "limón":
                        input("Escriba papas, naranjas o limon degún lo que desee llevar")
                    elif opC == "papas":
                        compra = compra + papas
                    elif opC == "limon" or opC == "limón":
                        compra = compra + limon
                    elif opC == "naranjas":
                compra = compra + naranjas
        elif op == 2:
            try:
                print(f"Su total de compra {compra}")
                pago = int(input(f"Ingrese su monto a pagar, no puede ser mayor que {compra}: "))
                if pago > compra:
                    int(input(f"su monto a pagar no puede ser mayor que {compra}, ingrese de nuevo: "))

                por_pagar = compra - pago
            except ValueError:
                input("Escriba sólo números")
    except ValueError:  
        int(input("ingrese la opcion en forma de numero")) 






