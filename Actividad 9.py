def agregar_pelicula(peliculas):
    cantidad_peliculas = int(input("Ingrese la cantidad de películas que agregará: "))
    for i in range(cantidad_peliculas):
        print(f"Película {i+1}:")
        titulo = input("Ingrese el título de la pelicula: ")
        anio = input("Ingrese el año en el que se estrenó: ")
        genero = input("Ingrese el género de la película: ").lower()
        pelicula = [titulo, anio, genero]
        peliculas.append(pelicula)
def mostrar_peliculas(peliculas):
    if not peliculas:
        print("No hay películas guardadas")
    else:
        print("\nPelículas:")
        for p in peliculas:
            print(f"Título: {p[0]}, Año: {p[1]}, Género: {p[2]}")
def buscar_genero(peliculas):
    genero = input("Ingrese el género a buscar: ").lower()
    print(f"\nPelículas del género '{genero}':")
    contador = 0
    for p in peliculas:
        if p[2] == genero:
            print(f"Título: {p[0]}, Año: {p[1]}")
            contador += 1
    if contador == 0:
        print("No hay registradas películas con ese género")
def eliminar_titulo(peliculas):
    titulo = input("Ingrese el título de la película a eliminar de forma exacta: ").strip().lower()
    for t in peliculas:
        if t[0].lower() == titulo.lower():
            peliculas.remove(t)
            print("Película eliminada, con éxito")
            return
    print("No se encontró ninguna película con ese título")
def estadisticas_peliculas(peliculas):
    print(f"\nTotal de películas: {len(peliculas)}")
    generos = []
    print("Películas por género:")
    for p in peliculas:
        if p[2] not in generos:
            generos.append(p[2])
            cantidad = 0
            for x in peliculas:
                if x[2] == p[2]:
                    cantidad += 1
            print(f"{p[2].capitalize()}: {cantidad}")
    if peliculas:
        mas_antigua = peliculas[0]
        for p in peliculas:
            if p[1] < mas_antigua[1]:
                mas_antigua = p
        print(f"Película más antigua es: {mas_antigua[0]} ({mas_antigua[1]})")
peliculas = []
while True:
    print("\n---BIENVENID@ AL MENÚ DE GESTOR DE PELÍCULAS---\n"
          "1.- Agregar películas\n"
          "2.- Mostrar todas las películas registradas\n"
          "3.- Buscar películas por género\n"
          "4.- Eliminar una película por título\n"
          "5.- Ver estadísticas del catálogo\n"
          "6.- Salir del programa")
    opciones = input("Por favor escriba el número de la opción que desea seleccionar: ")
    match opciones:
        case "1":
            agregar_pelicula(peliculas)
        case "2":
            mostrar_peliculas(peliculas)
        case "3":
            buscar_genero(peliculas)
        case "4":
            eliminar_titulo(peliculas)
        case "5":
            estadisticas_peliculas(peliculas)
        case "6":
            print("Programa terminado, muchas gracias por utilizarlo")
            break
        case _:
            print("Opción no válida, ingrese de nuevo")