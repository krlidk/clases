ventas = 0
print("Te damos la bienvenida a nuestro local.\n 1. Corte de pelo infante $5000. \n 2. Corte de pelo adulto $10000.\n 3. Corte de pelo adulto mayor $4000.\n 4. Salir.")
op = int(input("Por favor seleccione una de las opciones"))
try: 
     op = int(input("Por favor seleccione una de las opciones: "))
except ValueError:
    print("Debe ingresar un número: ")

while op != 4:
    if op < 1 or op >4:
    print("Debe ingresar un número del 1 al 4")
    try: 
        op = int(input("Por favor seleccione una de las opciones: "))
    except ValueError:
        print("Debe ingresar un número: ")
    try: 
        op = int(input("Por favor seleccione una de las opciones: "))
    except ValueError:
        print("Debe ingresar un número: ")

    edad=int(input("Ingrese su edad: "))
    try:

