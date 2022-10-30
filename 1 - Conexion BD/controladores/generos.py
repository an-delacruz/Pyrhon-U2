from DTO.generos import Generos
from logger import log
from modelos.genero import Genero


def MostrarGeneros():
    generos = Generos.getAll()
    if not generos:
        print('No hay generos')
        return
    print('Listado de generos')
    print('ID\tNombre')
    for genero in generos:
        print(f'{genero.id}\t{genero.nombre}')


def MostrarGenero():
    id = input('Ingrese el ID del genero: ')
    genero = Generos.getByPK(id)
    if not genero:
        print('El genero no existe')
        return
    print('Genero')
    print('ID\tNombre')
    print(f'{genero.id}\t{genero.nombre}')


def AgregarGenero():
    nombre = input('Ingrese el nombre del genero: ')
    genero = Genero(nombre)
    Generos.create(genero)
    print('Genero agregado')


def EditarGenero():
    id = input('Ingrese el ID del genero: ')
    genero = Generos.getByPK(id)
    if not genero:
        print('El genero no existe')
        return
    nombre = input(f'Ingrese el nombre del genero ({genero.nombre}): ') or genero.nombre
    genero = Genero(nombre)
    Generos.updateByPK(id, genero)
    print('Genero editado')


def EliminarGenero():
    id = input('Ingrese el ID del genero: ')
    genero = Generos.getByPK(id)
    if not genero:
        print('El genero no existe')
        return

    res = Generos.deleteByPK(id)

    if res:
        log.debug(f"Se eliminó el genero {genero}")
        print('Genero eliminado')
    else:
        print('No se eliminó el genero')


def MenuGenero():
    opcion = input(
        '[1] Mostrar generos\n[2] Mostrar genero\n[3] Agregar genero\n[4] Editar genero\n[5] Eliminar genero\n[6] Volver al menu principal\nIngrese una opcion: ')

    if opcion == '1':
        MostrarGeneros()
    elif opcion == '2':
        MostrarGenero()
    elif opcion == '3':
        AgregarGenero()
    elif opcion == '4':
        EditarGenero()
    elif opcion == '5':
        EliminarGenero()
    elif opcion == '6':
        return
    else:
        print('Opcion no valida')
        MenuGenero()
