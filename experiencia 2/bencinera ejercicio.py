print("Te damos la bienvenida a la estación de bencina.") #se da la bienvenida

bencina = int(input("¿Cuántos litros de bencina tiene tu auto?  ")) #se pregunta cantidad de bencina, como entero
if bencina<10:
    print("Cargue más bencina")
    tipo = input("¿Qué tipo de bencina desea cargar? 93, 95, 97  ")
    if tipo == 93:
        print("Se esta cargando bencina regular")
    else:
        if tipo ==95:
             print("Se esta cargando bencina plus")
        else:
            if tipo ==97:
                print("Se esta cargando bencina premium")   
            else:
                print("Opcion no valida, intentelo de nuevo")
else:
    print("No necesita cargar bencina.")

