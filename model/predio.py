from utils.db import db

from dataclasses import dataclass

@dataclass
class Predio(db.Model):
    id_predio: int
    id_tipo_predio: int
    descripcion: str
    ruc: str
    telefono: str
    correo: str
    direccion: str
    idubigeo: str

    
    id_predio=db.Column(db.Integer, primary_key=True)
    id_tipo_predio=db.Column(db.Integer)
    descripcion=db.Column(db.String(120))
    ruc=db.Column(db.String(12))
    telefono=db.Column(db.String(15))
    correo=db.Column(db.String(50))
    direccion=db.Column(db.String(50))
    idubigeo=db.Column(db.String(10))

    
    def __init__(self, id_tipo_predio,descripcion,ruc,telefono,correo,direccion, idubigeo):
        self.id_tipo_predio=id_tipo_predio
        self.descripcion=descripcion
        self.ruc=ruc
        self.telefono=telefono
        self.correo=correo
        self.direccion=direccion
        self.idubigeo=idubigeo
        pass
