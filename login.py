from Server import db

class Login(db.Model):
    Id = db.Column(db.Integer, primary_key=True, nullable=False)
    login = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(12), nullable=False)

db.create_all()