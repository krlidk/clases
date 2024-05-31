from typing import Match

respuesta = int(input("Ingresa 1 o 2"))
contador = 0

match respuesta:
    case 1:
        print("Ha ingresado el número 1") #usuario ingresa num 1
    case 2:
        print("Ha ingresado el número 2") #usuario ingresa num 2
    case _:
        print("Ha ingresado otro número") #es un caso por defecto, _ = por defecto

        contador = contador + 1 #contadores igual que en pseint


#variables dentro de string es print(f"bkabka{variable}")
#al presionar alt se puede poner para escribir en varios sitios

# nombre-variable.lower=  hace que pase a minuscula y se lea igual

