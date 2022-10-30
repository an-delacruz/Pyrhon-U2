class Libro:
    def __init__(self, titulo, autor, anio_publicacion, genero, id=0):
        self._id = id
        self._titulo = titulo
        self._autor = autor
        self._anio_publicacion = anio_publicacion
        self._genero = genero

    @classmethod
    def fromTuple(cls, libro):
        return cls(libro[1], libro[2], libro[3], libro[4], id=libro[0])

    # Getters y Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, value):
        self._titulo = value

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, value):
        self._autor = value

    @property
    def anio_publicacion(self):
        return self._anio_publicacion

    @anio_publicacion.setter
    def anio_publicacion(self, value):
        self._anio_publicacion = value

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, value):
        self._genero = value

    def __str__(self):
        return "ID: %s, Título: %s, Autor: %s, Año: %s, Género: %s" % (
            self._id, self._titulo, self._autor, self._anio_publicacion, self._genero)
