op = int(input("Te damos la bienvenida a nuestra tienda, elige una opción. \n 1. COmprar \n 2. Pagar \n 3. Salir "))
compra = 0
papas = 2000
limon = 1000
naranjas = 1000

while op != 3:
    try:
        if op != 1 or op != 2 or op !=3:
            op = int(input("Eliga una opcion del 1 al 3: 1"))
    except ValueError:  
        int(input("ingrese la opcion en forma de numero")) 
