menu=""" Elija una de las opciones
1. Añadir libro.
2. Buscar libro.
3. Eliminar libro.
4. Salir.    """
op=None #variable de opcion
libros=[] #lista de los libros
autores=[] #lista de los autores
cantidad=0 #cantidad de libros a agregar
posición=0 #para buscar/eliminar autores en misma posición q el libro
eliminar=None #variable con el libro a eliminar
buscar=None #variable con el libro a buscar
while True:
    print(menu) #se dan las opciones y se pide la opción
    op=input("ingrese su opción elegida:  ")
    match op:
        case "1": #entra a agregar libros
            try:
                cantidad=int(input("cuantos libros desea agregar?"  )) #se pide al usuario cantidad de libros a agregar
                for i in range(cantidad):
                    agregar_libro=input("Agrege el título del libro: ")
                    libros.append(agregar_libro) #se pide y agrega el titulo del libro
                    agregar_autor=input("Agrege el nombre del autor:  ")
                    autores.append(agregar_autor) #se pdie y agrega el autor del libro
                    print("libro agregado con éxito  \n")
            except ValueError:
                print("valor ingresado no válido \n")
        case "2": #entra a buscar libros
            buscar=input("Busque un libro agregando su nombre:  ") #se pide el libro a buscar
            if buscar in libros: #revisa si ese libro está en la lista 
                for i in libros:
                    if buscar == i:
                        posicion=libros.index(i) #busca su posición en la lista para buscarlo en el autor agregado en la misma posición
                        print(f"Su libro es {i} y su autor es {autores[posicion]} \n")
            else:
                print("El libro no está en la lista. \n")
        case "3": #entra a eliminar libros
            eliminar = input("Ingrese el nombre del libro a eliminar: ")
            if eliminar in libros: #corrobora que esté en la lista
                posicion = libros.index(eliminar) #para saber la posición del libro
                libros.pop(posicion) #elimina el autor y el libro que comparten posición
                autores.pop(posicion)
                print("Libro borrado con éxito \n")
            else:
                print("El libro no está en la lista. \n")
        case "4": #opción para salir
            print("Hasta la próxima")
            break
        case _: #en caso de que el usuario agrege cualquier otra opción
            print("por favor ingrese su opción poniendo el numero a elegir \n")