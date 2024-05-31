print("Te damos la bienvenida a nuestro local.\n 1. Corte de pelo infante $5000. \n 2. Corte de pelo adulto $10000.\n 3. Corte de pelo adulto mayor $4000.\n 4. Salir.")
ventas = 0
infante=5000
adulto=10000
mayor=4000
op = 0
while op != 4:
    try:
         op = int(input("Por favor seleccione una de las opciones: "))
         if op==1:
              try:
                    edad=int(input("Ingrese su edad: "))
                    if edad>15 and edad<0:
                         print("no eres un infante")
                    else:
                        if edad>0 and edad<=15:
                             ventas=ventas+infante
                             print(f"Se ha realizado el corte de pelo, su total es {ventas}")
               except ValueError:
                   print("debe ingresar un número")
          if op==2:
              
               