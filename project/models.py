from project import db

class BaseModel():

	# def __init__(self, a):
	# 	if len(a) > 1:
	# 		for i in range(1, len(a)):
	# 			self.i = i

	def serialize(self):
		r = {}
		for i in self.a:
			r[i] = getattr(self,i)
		if self.land != None:
			r['land_name'] = self.land.name
		else:
			r['land_name'] = None		
		if self.attraction != None:
			r['attraction_name'] = self.attraction.name
		else:
			r['attraction_name'] = None			
		return r				

class Parks(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	lands = db.relationship('Lands', backref='parks')
	attractions = db.relationship('Attractions', backref='parks')
	mickeys = db.relationship('Mickeys', backref='parks')
	a = ['id', 'name']

	def __init__(self, name):
		self.name = name

class Lands(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	name = db.Column(db.Text, nullable=False)
	attractions = db.relationship('Attractions', backref='lands')
	mickeys = db.relationship('Mickeys', backref='lands')
	a = ['id', 'park_id', 'name']

	def __init__(self, park_id, name):
		self.park_id = park_id
		self.name = name

class Attractions(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	land_id = db.Column(db.Integer, db.ForeignKey('lands.id'))
	name = db.Column(db.Text, nullable=False)
	mickeys = db.relationship('Mickeys', backref='attractions')
	a = ['id', 'park_id', 'land_id', 'name']

	def __init__(self, park_id, land_id, name):
		self.park_id = park_id
		self.land_id = land_id
		self.name = name

class Mickeys(BaseModel, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	park_id = db.Column(db.Integer, db.ForeignKey('parks.id'))
	land_id = db.Column(db.Integer, db.ForeignKey('lands.id'))
	land = db.relationship('Lands', foreign_keys='Mickeys.land_id')
	attraction_id = db.Column(db.Integer, db.ForeignKey('attractions.id'))
	attraction = db.relationship('Attractions', foreign_keys='Mickeys.attraction_id')
	photo_url = db.Column(db.Text)
	description = db.Column(db.Text)
	hint = db.Column(db.Text)
	a = ['id', 'park_id', 'land_id', 'attraction_id', 'photo_url', 'description', 'hint']

	def __init__(self, park_id, land_id, attraction_id, photo_url, description, hint):
		self.park_id = park_id
		self.land_id = land_id
		self.attraction_id = attraction_id
		self.photo_url = photo_url
		self.description = description
		self.hint = hint					