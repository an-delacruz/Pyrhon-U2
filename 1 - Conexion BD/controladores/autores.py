from DTO.autores import Autores
from logger import log
from modelos.autor import Autor


def MostrarAutores():
    autores = Autores.getAll()
    if not autores:
        print('No hay autores registrados')
        return
    print('Listado de autores')
    print('ID\tNombre\tApellido\tNacionalidad')
    for autor in autores:
        print(f'{autor.id}\t{autor.nombre}\t{autor.apellido}\t{autor.nacionalidad}')


def MostrarAutor():
    id = input('Ingrese el ID del autor: ')
    autor = Autores.getByPK(id)
    if not autor:
        print('El autor no existe')
        return
    print('Autor')
    print(f'ID: {autor.id}\tNombre: {autor.nombre}\tApellido: {autor.apellido}\tNacionalidad: {autor.nacionalidad}')


def AgregarAutor():
    nombre = input('Ingrese el nombre del autor: ')
    apellido = input('Ingrese el apellido del autor: ')
    nacionalidad = input('Ingrese la nacionalidad del autor: ')
    autor = Autor(nombre, apellido, nacionalidad)
    res = Autores.create(autor)
    if res > 0:
        print('Autor agregado')
    else:
        print('No se agregó el autor')


def EditarAutor():
    id = input('Ingrese el ID del autor: ')
    autor = Autores.getByPK(id)
    if not autor:
        print('El autor no existe')
        return
    nombre = input(f'Ingrese el nombre del autor ({autor.nombre}): ') or autor.nombre
    apellido = input(f'Ingrese el apellido del autor ({autor.apellido}): ') or autor.apellido
    nacionalidad = input(f'Ingrese la nacionalidad del autor ({autor.nacionalidad}): ') or autor.nacionalidad
    autor = Autor(nombre, apellido, nacionalidad)
    res = Autores.updateByPK(id, autor)
    if res:
        print('Autor editado')
    else:
        print('No se editó el autor')


def EliminarAutor():
    id = input('Ingrese el ID del autor: ')
    autor = Autores.getByPK(id)
    if not autor:
        print('El autor no existe')
        return

    res = Autores.deleteByPK(id)

    if res:
        log.debug(f'Se elimino el autor {autor}')
        print('Autor eliminado')
    else:
        print('No se eliminó el autor')


def MenuAutor():
    opcion = input(
        '[1] Mostrar autores\n[2] Mostrar autor\n[3] Agregar autor\n[4] Editar autor\n[5] Eliminar autor\n[6] Volver\nIngrese una opcion: ')
    if opcion == '1':
        MostrarAutores()
    elif opcion == '2':
        MostrarAutor()
    elif opcion == '3':
        AgregarAutor()
    elif opcion == '4':
        EditarAutor()
    elif opcion == '5':
        EliminarAutor()
    elif opcion == '6':
        return
    else:
        print('Opción inválida')
        MenuAutor()
