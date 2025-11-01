from loja import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=False, nullable="False")
    username = db.Column(db.String(40), unique=True, nullable="False")
    email = db.Column(db.String(120), unique=True, nullable="False")
    password = db.Colum(db.String(180), unique=False, nullable="False")
    profile = db.Colum(db.String(180), unique=False, nullable="False", default=".profile.jpg")

    def __repr__(self):
        return f'<User {self.name!r}>'

db.create_all()