class Genero:
    def __init__(self, nombre, id=0):
        self._id = id
        self._nombre = nombre

    @classmethod
    def fromTuple(cls, genero):
        return cls(genero[1], id=genero[0])

    # Getters y Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    def __str__(self):
        return "ID: %s, Nombre: %s" % (self._id, self._nombre)
