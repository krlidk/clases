print("Te damos la bienvenida a nuestro local.\n 1. Corte de pelo infante $5000. \n 2. Corte de pelo adulto $10000.\n 3. Corte de pelo adulto mayor $4000.\n 4. Salir.")
op = int(input("Elige una opción: "))
if op >= 1 or op <=4:
    while op != 4:
        edad=int(input("Ingrese su edad: "))
        if edad > 0 and edad <= 15:
            


