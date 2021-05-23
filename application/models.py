from application import db

class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    art = db.Column(db.String(50), nullable = False)
    wins = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String(50), nullable = False)
    qoute = db.Column(db.String(300), nullable = False)
    