try:
    edad = int(input("ingrese su edad: "))
    if edad >= 18:
        print("eres mayor de edad")
    else:
        print("eres menor de edad")
except ValueError:
    print("Ingrese sólo números en forma de digitos")