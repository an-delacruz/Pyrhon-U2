from conexion.cursor import CursorPool as Pool
from modelos.genero import Genero


class Generos:
    @staticmethod
    def getAll():
        try:
            with Pool() as pool:
                pool.execute("Select * from Generos")
                generos = [Genero.fromTuple(genero) for genero in pool.fetchall()]
                return generos
        except Exception as e:
            return None

    @staticmethod
    def getByPK(id):
        try:
            with Pool() as pool:
                pool.execute("Select * from Generos where id = %s", (id,))
                genero = Genero.fromTuple(pool.fetchone())
                return genero
        except Exception as e:
            return None

    @staticmethod
    def create(genero=Genero):
        try:
            with Pool() as pool:
                pool.execute('Insert into Generos (nombre) values (%s)', (genero.nombre,))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def updateByPK(id, genero=Genero):
        try:
            with Pool() as pool:
                pool.execute('Update Generos set nombre = %s where id = %s', (genero.nombre, id))
                return pool.rowcount
        except Exception as e:
            return None

    @staticmethod
    def deleteByPK(id):
        try:
            with Pool() as pool:
                pool.execute('Delete from Generos where id = %s', (id,))
                return pool.rowcount
        except Exception as e:
            return None
