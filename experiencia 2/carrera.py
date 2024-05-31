print("comienza la carrera")

respuesta=input("¿encontraste una valla? Si/No")
if respuesta == "Si":
    print("Salta la valla")
else:
    if respuesta == "No":
        print("Siga corriendo.")

respuesta=input("¿encontraste un tunel? Si/No")
if respuesta == "Si":
    print("Atraviesa el tunel")
else:
    if respuesta == "No":
        print("Siga corriendo.")

espuesta=input("¿encontraste una laguna? Si/No")
if respuesta == "Si":
    print("Te agotas al nadar y pierdes.")
else:
    if respuesta == "No":
        print("¡Usted ha terminado la carrera!")

