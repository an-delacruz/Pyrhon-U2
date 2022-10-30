from app import db

class Chofer(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    telefono = db.Column(db.String(250))
    licencia = db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Nombre: {self.nombre},'
                f'Apellido: {self.apellido},'
                f'telefono: {self.telefono},'
                f'licencia: {self.licencia}')
        
class Tractor(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.String(250))
    placas=db.Column(db.String(250))
    marca=db.Column(db.String(250))
    modelo=db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Numero: {self.numero},'
                f'Placas: {self.placas},'
                f'Marca: {self.marca},'
                f'Modelo: {self.modelo}')

class Remolque(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    numero=db.Column(db.String(250))
    placas=db.Column(db.String(250))
    tipo=db.Column(db.String(250))
    
    def __str__(self) -> str:
        return (f'ID: {self.id},'
                f'Numero: {self.numero},'
                f'Placas: {self.placas},'
                f'Tipo: {self.tipo}')