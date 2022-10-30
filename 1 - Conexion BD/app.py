from conexion.cursor import CursorPool as Pool
from controladores import libros, autores, generos
from logger import log

if __name__ == '__main__':
    with Pool() as pool:
        pool.execute("SELECT 1")
        res, = pool.fetchone()
        if res == 1:
            log.debug("Se establecio conexion con la base de datos")
            print("Conexion exitosa")
        else:
            print("Conexion ")
            exit()

    while 1 == 1:
        print("Menu")
        opcion = input('[1] Libros\n[2] Autores\n[3] Generos\n[4] Salir\nOpcion: ')

        if opcion == '1':
            libros.MenuLibro()
        elif opcion == '2':
            autores.MenuAutor()
        elif opcion == '3':
            generos.MenuGenero()
        elif opcion == '4':
            exit()
