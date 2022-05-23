from Dominio.Pelicula import Pelicula
from Servicio.CatalogoPeliculas import CatalogoPeliculas

opcion = None
while opcion != 4:
    try:
        print("1) Agregar pelicula")
        print("2) Listar peliculas")
        print("3) Eliminar catalogo peliculas")
        print("4) salir")

        opcion = int(input("Escribe tu opcion (1 - 4):"))

        if opcion == 1:
            nombre_pelicula = input("Proporciona el nombre de la pelicula: ")
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()

    except Exception as e:
        print(f"ocurrio un error {e}")
        opcion = None
else:
    print("Salimos del programa...")
