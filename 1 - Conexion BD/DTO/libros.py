from conexion.cursor import CursorPool as Pool
from modelos.libro import Libro


class Libros:
    @staticmethod
    def getAll():
        try:
            with Pool() as pool:
                pool.execute("Select  id, titulo, autor, anio_publicacion, genero from Libros")
                libros = [Libro.fromTuple(libro) for libro in pool.fetchall()]
                return libros
        except Exception as e:
            return None

    @staticmethod
    def getByPK(id):
        try:
            with Pool() as pool:
                pool.execute("Select id, titulo, autor, anio_publicacion, genero from Libros where id = %s", (id,))
                libro = Libro.fromTuple(pool.fetchone())
                return libro
        except Exception as e:
            return None

    @staticmethod
    def create(libro=Libro):
        try:
            with Pool() as pool:
                pool.execute('Insert into Libros (titulo, autor, anio_publicacion, genero) values (%s, %s, %s, %s)',
                             (libro.titulo, libro.autor, libro.anio_publicacion, libro.genero))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def updateByPK(id, libro=Libro):
        try:
            with Pool() as pool:
                pool.execute(
                    'Update Libros set titulo = %s, autor = %s, anio_publicacion = %s, genero = %s where id = %s',
                    (libro.titulo, libro.autor, libro.anio_publicacion, libro.genero, id))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def deleteByPK(id):
        try:
            with Pool() as pool:
                pool.execute('Delete from Libros where id = %s', (id,))
                return pool.rowcount
        except Exception as e:
            return None
