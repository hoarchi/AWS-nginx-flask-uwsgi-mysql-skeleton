from app import db

db.create_all()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	location = db.Column(db.String(255))
	category = db.Column(db.String(255))

