from project import db

class Parks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	lands = db.relationship('Lands', backref='person')

	def __init__(self, name):
		self.name = name

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name
		}

class Lands(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	name = db.Column(db.Text, nullable=False)

	def __init__(self, park_id, name):
		self.park_id = park_id
		self.name = name

	def serialize(self):
		return {
			'id': self.id,
			'parkId': self.park_id,
			'name': self.name
		}	