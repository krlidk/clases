total=0
while True:
    #clave son 5 num del primer jugador
    clave = input("ingresa una clave de 5 numeros: ")
    largo = len(clave) #largo es los digitos de la clave

    if largo != 5:
        print("la clave ingresada debe tener 5 digitos ")
    else:
        print("--Comienza el juego--")
        for i in range(largo):
            guess = input(f"ingrese digino n° {i+1}: ") #guess es el digito del jugador 2
            if guess == clave[i]:
                print(f"Felicidades Adivinaste el digito correctamente en la posicion {i+1}")
                totat=total+1
            else:
                print("intentalo de nuevo ")
            
    if total == 5:
        print(f"Felicidades adivinaste los todos los numeros , la clave a adivinar es {clave}")
        break
    else:
        print(f"Lo siento intentalo de nuevo el numero a adivinar era {clave} ")
        break