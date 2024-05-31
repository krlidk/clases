from typing import Match

resp = input("¿Cual de los siguientes animales vive en el agua? perro, cocodrilo, conejo o tiburón: ")
puntos=0
match resp:
    case "cocodrilo":
        puntos = puntos + 0.5
    case "tiburón":
        puntos = puntos + 1.0
    case _:
        puntos = 0

print(f"Su puntaje obtenido es: {puntos}")
