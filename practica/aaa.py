menu = """Bienvenido, elija una de las siguientes opciones: 
1-. Comprar
2-. Pagar
3-. Salir  """
precios = """elija que desea comprar:
Papas 3kg a $2000
kilo de naranjas a $1000
kilo de limón a $1000    """
while True:
    monto = 0
    cuenta = 0
    op = input(menu)
    if op == "1":
        compra = input(precios)
        compra = (compra.lower)
        match compra:
            case "papas":
                monto = (monto+2000)
            case "limon":
                monto = (monto+1000)
            case "limón":
                monto = (monto+1000)
            case "naranjas":
                  monto = (monto+1000)
            case _:
                print("ingrese el nomnbre de lo que desee comprar")
    else:
         if op == "2":
            try:
                pago = int(input(f"Su total a pagar es: {monto}, ¿Cuánto desea pagar?"))
                if pago > monto or pago < 0:
                    print("Debe ingresar un monto mayor a 0 y menor o igual a su cuenta")
                elif pago < monto or pago > 0:
                    cuenta = monto - pago
                    print(f"Su cuenta ha quedado en: {cuenta}")
            except ValueError:
                    print("ingrese el monto en números")
            else:
                if op == "3":
                    print(f"gracias por comprar en nuestra verduleia")
                    break
                else:
                    print("Elija una de las opciones. 1-2-3")