discoDuro=10
ram=3
PlacaM=10
FuentePoder=0
admin = "a"
contra_admin = "a"
usuario=None
contra_usu=None
op=0
opci=0

while True:
    op=input("1.Iniciar sesión \n 2.Salir  ")
    match op:
        case "1":
            valid_usu=input("ingrese su usuario: ")
            valid_contra=input("ingrese su clave: ")
            if valid_usu==contra_admin and valid_contra==contra_admin:
                while opci!="4":
                    opci=input("1.Dar de alta usuasrio\n 2.Abastecer locar\n 3.Sacar reporte\n Cerrar sesión")
                    if opci!="1" and opci!="2" and opci!="3" and opci!="4":
                        print("elija una de las opciones. 1-2-3-4")
                    elif opci=="1":
                        usuario=input("Cree el nombre de usuario: ")
                        contra_usu=input("cree la clave del usuario: ")
                    elif opci=="2":
                        try:
                            abastecimiento=input("Cuantos productos desea abastecer? ")
                            abastecimiento=abastecimiento.strip
                            abastecimiento=abastecimiento.lower
                            for i in range(abastecimiento):
                                producto=input("qué producto desea abastecer? ")
                                cantidad=int(input("cuántos desea agregar? "))
                                if producto=="discoduro":
                                    discoDuro=discoDuro+cantidad
                                if producto=="memoriasram":
                                    ram=ram+cantidad
                                if producto=="placasmadre":
                                    PlacaM=PlacaM+cantidad
                                if producto=="fuetesdepoder":
                                    FuentePoder=FuentePoder+cantidad
                        except ValueError:
                            print("ingrese numeros al ingresar cantidad de productos a agregar")
                    elif opci=="3":
                        print(f"El total de productos es:\n Disco duro={discoDuro}\n Placas madre={PlacaM}\n memorias ram={ram}\n fuentes de poder={FuentePoder}")
                    elif opci=="4":
                        print("Saliendo del menú administrador")
                        break
            elif valid_usu==usuario and valid_contra==contra_usu:
                while opci!="4":
                    opci=input("Bienvenido a Computer factory, escoja una opción:\n 1.Comprar productos\n 2.Pagar cuenta\n 3. Cerrar sesión\n -------\n   ")
                    if opci=="1":
                        