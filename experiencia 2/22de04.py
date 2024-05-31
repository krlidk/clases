
#for i in range(veces a repetir)
veces = int(input("Ingrese veces a repetir"))
 
for i in range(veces):
    print(f"Ejecución {veces}")


#while
op = 1
print ("Bienvenido")

while op != 3:
    print ("opcion 1: comprar \n opcion 2: vender \n opcion 3: salir")
    op = int(input("Escoja una opción:  "))
    