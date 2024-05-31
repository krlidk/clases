clave = input("Ingrese una clave secreta de 5 dígitos: ")
for i in clave:
    print(i.strip)

largo = len(clave.strip)

if largo != 5:
    input("Su clave tiene que ser de 5 dígitos: ")

intentos = 6
while intentos < 0:
    resp = input("Ingrese numeros del 0 al 9 para adivinar la clave secreta: ")
    resp1 = int(resp)
    # resp es texto y resp 1 es numeros
    if resp1 < 0 or resp1 > 9:
        print("Ingrese números del 0 al 9")
    
