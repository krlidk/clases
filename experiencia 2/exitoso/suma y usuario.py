import getpass

menu = """1. Ingresar usuario
2. Iniciar suma
3. Salir """
total = 0
while True:
    op = (input(menu))
    if op != "1" and op != "2" and op != "3":
        print("Elija una de las  opciones. (1, 2 o 3)")
    else:
        match op:
            case "1":
                usser = input("registre su usuario: ")
                print("registre su contraseña: ")
                clave = getpass.getpass()
            case "2": 
                valid_usser = input("ingrese su usuario: ")
                valid_clave = input("Ingrese su clave: ")
                if valid_usser == usser and valid_clave == clave:
                    try:
                        sumas = int(input("Ha ingresado con exito, cuantas veces desea hacer suma? "))
                        for i in range(sumas):
                            sumando = int(input("Ingrese el número a sumar: "))
                            total = total + sumando
                    except ValueError:
                        print("ingrese números")
                else:
                    print("Usuario y/o contraseña incorrecta, intente de nuevo")
            case "3":
                print(f"El total de sus sumas es: {total}")
                break