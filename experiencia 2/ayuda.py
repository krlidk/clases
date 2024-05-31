import getpass
usu1 = None
usu2 = None
usu3 = None
contra1 = None
contra2 = None
contra3 = None
op = 0
opci=0
while op != 3:
    op = input("1. Iniciar sesión \n 2.Registrar usuario \n 3.Salir   ")
    if op == "1":
        valid_usu = input("Ingrese su usuario: ") #pidiendo al usuario ingresar
        valid_contra = input("Ingrese su clave: ")

        if usu1==None: #si no se ha sobreescrito la variable de usuarios dice de registrarse primero
            print("Usuario no registrado")
        elif usu1==valid_usu and contra1==valid_contra: #el usuario entra al segudno menú
            while opci!="3":
                opci=input("1.relizar llamada\n2.Enviar correo electrónico\n 3.Cerrar sesión    ")
                if opci=="1":
                    try:
                        cel = int(input("Ingrese un número de celular: "))
                        cel=str(cel)
                        largo=len(cel.strip())
                        largo= int(largo)
                        prim=cel[0]
                        if largo == 9 and prim == "9": #validando largo del numero dado, sin el 9
                            print("su número ha sid ingresado correctamente")
                        elif largo != 9 or prim != "9":
                            print("ingrese 9 dígitos, el primero debe ser un 9")
                    except ValueError:
                        print("ingrese solo numeros")
                if opci=="2":
                    while True:
                        correo=input("ingrese su correo electrónico:  ")
                        arroba = False
                        for i in correo:
                            if i == "@": #validando el @ en el correo
                                arroba=True
                                break
                        if arroba:
                            print("Correo electrónico válido.")
                            mensaje=input("ingrese el mensaje a enviar")
                            break
                        else:
                            print("El correo electrónico debe contener al menos un '@'. Inténtelo de nuevo.")
                if opci=="3":
                    print("Cerrando sesión")
    elif op == "2":
        usu1 = input("registre su usuario: ")
        print("registre su contraseña: ")
        contra1 = getpass.getpass()
    elif op == "3":
        print("saliendo del programa")
        break
    elif op != "1" or op != "2" or op != "3":
        op=input("error, ingrese 1-2-3 según la opción que desee.")