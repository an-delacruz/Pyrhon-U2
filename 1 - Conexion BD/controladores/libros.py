from DTO.autores import Autores
from DTO.generos import Generos
from DTO.libros import Libros
from logger import log
from modelos.libro import Libro


def MostrarLibros():
    libros = Libros.getAll()
    if not libros:
        print('No hay libros')
        return
    print('Listado de libros')
    print('ID\tTitulo\t\tAutor\tAño\tGenero')
    for libro in libros:
        print(f'{libro.id}\t{libro.titulo}\t{libro.autor}\t{libro.anio_publicacion}\t{libro.genero}')


def MostrarLibro():
    id = input('Ingrese el ID del libro: ')
    libro = Libros.getByPK(id)
    if not libro:
        print('El libro no existe')
        return
    print('Libro')
    print('ID\tTitulo\tAutor\tAño\tGenero')
    print(f'{libro.id}\t{libro.titulo}\t{libro.autor}\t{libro.anio_publicacion}\t{libro.genero}')


def AgregarLibro():
    titulo = input('Ingrese el titulo del libro: ')
    print("Autores disponibles [0-10]")
    autores = Autores.getAll()[0:10]
    print("ID\tNombre")
    for autor in autores:
        print(f"{autor.id}\t{autor.nombre}")

    autor = input('Ingrese el autor del libro: ')
    año = input('Ingrese el año del libro: ')
    print("Generos disponibles [0-10]")
    generos = Generos.getAll()[0:10]
    print("ID\tNombre")
    for genero in generos:
        print(f"{genero.id}\t{genero.nombre}")

    genero = input('Ingrese el genero del libro: ')
    libro = Libro(titulo, autor, año, genero)
    Libros.create(libro)
    print('Libro agregado')


def EditarLibro():
    id = input('Ingrese el ID del libro: ')
    libro = Libros.getByPK(id)
    if not libro:
        print('El libro no existe')
        return
    titulo = input(f'Ingrese el titulo del libro ({libro.titulo}): ') or libro.titulo
    print("Autores disponibles [0-10]")
    autores = Autores.getAll()[0:10]
    if not autores:
        print('No hay autores, registre uno primero')
        return
    print("ID\tNombre")
    for autor in autores:
        print(f"{autor.id}\t{autor.nombre}")

    autor = input(f'Ingrese el id del autor del libro ({libro.autor}): ') or libro.autor
    año = input(f'Ingrese el año del libro ({libro.anio_publicacion}): ') or libro.anio_publicacion

    print("Generos disponibles [0-10]")
    generos = Generos.getAll()[0:10]
    if not generos:
        print('No hay generos, registre uno primero')
        return
    print("ID\tNombre")
    for genero in generos:
        print(f"{genero.id}\t{genero.nombre}")

    genero = input(f'Ingrese el id del genero del libro ({libro.genero}): ') or libro.genero

    libro = Libro(titulo, autor, año, genero)
    res = Libros.updateByPK(id, libro)

    if res:
        print('Libro editado')
    else:
        print('No se editó el libro')


def EliminarLibro():
    id = input('Ingrese el ID del libro: ')
    libro = Libros.getByPK(id)
    if not libro:
        print('El libro no existe')
        return

    res = Libros.deleteByPK(id)

    if res:
        log.debug(f'Se elimino el libro {libro}')
        print('Libro eliminado')
    else:
        print('No se eliminó el libro')


def MenuLibro():
    opcion = input(
        '[1] Mostrar libros\n[2] Mostrar libro\n[3] Agregar libro\n[4] Editar libro\n[5] Eliminar libro\n[6] Volver al menu principal\nIngrese una opcion: ')

    if opcion == '1':
        MostrarLibros()
    elif opcion == '2':
        MostrarLibro()
    elif opcion == '3':
        AgregarLibro()
    elif opcion == '4':
        EditarLibro()
    elif opcion == '5':
        EliminarLibro()
    elif opcion == '6':
        return
    else:
        print('Opcion no valida')
        MenuLibro()
