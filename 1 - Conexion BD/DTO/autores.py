from conexion.cursor import CursorPool as Pool
from modelos.autor import Autor


class Autores:
    @staticmethod
    def getAll():
        try:
            with Pool() as pool:
                pool.execute("Select * from Autores")
                autores = [Autor.fromTuple(autor) for autor in pool.fetchall()]
                return autores
        except Exception as e:
            return None

    @staticmethod
    def getByPK(id):
        try:
            with Pool() as pool:
                pool.execute("Select * from Autores where id = %s", (id,))
                autor = Autor.fromTuple(pool.fetchone())
                return autor
        except Exception as e:
            return None

    @staticmethod
    def create(autor=Autor):
        try:
            with Pool() as pool:
                pool.execute('Insert into Autores (nombre,apellido, nacionalidad) values (%s,%s,%s)',
                             (autor.nombre, autor.apellido, autor.nacionalidad))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def updateByPK(id, autor=Autor):
        try:
            with Pool() as pool:
                pool.execute('Update Autores set nombre = %s, apellido = %s, nacionalidad = %s where id = %s',
                             (autor.nombre, autor.apellido, autor.nacionalidad, id))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def deleteByPK(id):
        try:
            with Pool() as pool:
                pool.execute('Delete from Autores where id = %s', (id,))
                return pool.rowcount
        except Exception as e:
            return None
