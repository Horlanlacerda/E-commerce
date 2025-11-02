from loja import db

class Marcas(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

class Categoria(db.Model):
    id = db.Collumn(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)

db.create_all()