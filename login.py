from Server import db

class Login(db.Model):
    login = db.Column(db.String(100), primary_key=True, nullable=False)
    nome = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    senha = db.Column(db.String(12), nullable=False)

db.create_all()