class Autor:
    def __init__(self, nombre, apellido, nacionalidad, id=0):
        self._id = id
        self._nombre = nombre
        self._apellido = apellido
        self._nacionalidad = nacionalidad

    @classmethod
    def fromTuple(cls, autor):
        return cls(autor[1], autor[2], autor[3], id=autor[0])

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

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @property
    def nacionalidad(self):
        return self._nacionalidad

    @nacionalidad.setter
    def nacionalidad(self, value):
        self._nacionalidad = value

    def __str__(self):
        return "ID: %s, Nombre: %s, Apellido: %s, Nacionalidad: %s" % (
            self._id, self._nombre, self._apellido, self._nacionalidad)
