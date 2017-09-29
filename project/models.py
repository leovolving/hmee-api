from project import db

class Parks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)

	def __init__(self, name):
		self.name = name

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name
		}