menu = """Bienvenido, elija una de las siguientes opciones: 
1-. Comprar
2-. Pagar
3-. Salir  """
precios = """elija que desea comprar:
Papas 3kg a $2000
kilo de naranjas a $1000
kilo de limón a $1000    """
monto = 0
cuenta = 0
while True:
    op = input(menu)
    match op:
        case "1":
            compra = input(precios)
            compra = (compra.lower)
            if compra == "papas":
                monto = (monto+2000)
            elif compra == "limon" or compra == "limón" or compra == "naranjas":
                monto = (monto+1000)
            else:
                print("ingrese el nomnbre de lo que desee comprar")
       
            if op == "1":
                compra = input(precios)
                compra = (compra.lower)
                if compra == "papas":
                    monto = (monto+2000)
                elif compra == "limon" or compra == "limón" or compra == "naranjas":
                    monto = (monto+1000)
                else:
                    print("ingrese el nomnbre de lo que desee comprar")
            case "2":
                try:
                    pago = int(input(f"Su total a pagar es: {monto}, ¿Cuánto desea pagar?"))
                    if pago > monto or pago < 0:
                        print("Debe ingresar un monto mayor a 0 y menor o igual a su cuenta")
                    else:
                        cuenta = monto - pago
                        print(f"Su cuenta ha quedado en: {cuenta}")
                except ValueError:
                    print("ingrese el monto en números")
            case "3":
                print(f"gracias por comprar en nuestra verduleia")
                break
