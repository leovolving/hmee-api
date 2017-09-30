from project import db
from project.models import Parks, Lands, Attractions, Mickeys
from flask import request, Blueprint, request, abort
from flask.json import jsonify

home_blueprint = Blueprint(
    'home', __name__
)

# use decorators to link the function to a url
@home_blueprint.route('/')
def home():
    return "Hello, World!"  # return a string

@home_blueprint.errorhandler(404)
def not_found(e):
	return abort(404)

"""
PARKS TABLE
"""

#All parks
@home_blueprint.route('/parks', methods=['GET'])
def parks():
	if request.method == 'GET':
		return jsonify(parks=[i.serialize() for i in Parks.query.all()])

#Parks by ID
@home_blueprint.route('/parks/<id>', methods=['GET'])
def parks_by_id(id):
	if request.method == 'GET':
		try:
			id = int(id)
			return jsonify(parks=[Parks.query.get(id).serialize()])	
		except (AttributeError, ValueError):
			return abort(404)				


"""
LANDS TABLE
"""

#All lands
@home_blueprint.route('/lands', methods=['GET'])
def lands():
	if request.method == 'GET':
		return jsonify(lands=[i.serialize() for i in Lands.query.all()])

#Lands by park id
@home_blueprint.route('/parks/<park_id>/lands', methods=['GET'])
def lands_by_park(park_id):
	if request.method == 'GET':
		return jsonify(lands=[i.serialize() for i in Lands.query.filter_by(park_id=park_id).all()])

#One land by ID
@home_blueprint.route('/lands/<id>', methods=['GET'])
def land_by_id(id):
	if request.method == 'GET':
		return jsonify(lands=[Lands.query.get(id).serialize()])	


"""
ATTRACTIONS TABLE
"""

#All attractions
@home_blueprint.route('/attractions', methods=['GET'])
def attractions():
	if request.method == 'GET':
		return jsonify(attractions=[i.serialize() for i in Attractions.query.all()])

#Attractions by land
@home_blueprint.route('/lands/<land_id>/attractions', methods=['GET'])
def attractions_by_land(land_id):
	if request.method == 'GET':
		return jsonify(attractions=[i.serialize() for i in Attractions.query.filter_by(land_id=land_id).all()])

#Attractions by park
@home_blueprint.route('/parks/<park_id>/attractions', methods=['GET'])
def attractions_by_park(park_id):
	if request.method == 'GET':
		return jsonify(attractions=[i.serialize() for i in Attractions.query.filter_by(park_id=park_id).all()])

#One attraction by ID
@home_blueprint.route('/attractions/<id>', methods=['GET'])
def attraction_by_id(id):
	if request.method == 'GET':
		return jsonify(attractions=[Attractions.query.get(id).serialize()])


"""
MICKEYS TABLE
"""

#All Mickeys/add Mickey
@home_blueprint.route('/mickeys', methods=['GET', 'POST'])
def mickeys():
	if request.method == 'GET':
		return jsonify(mickeys=[i.serialize() for i in Mickeys.query.all()])
	if request.method == 'POST':
		a = ['park_id', 'land_id', 'attraction_id', 'photo_url', 'description', 'hint']
		j = request.json
		for r in a:
			if r not in request.json:
				request.json[r] = None
		db.session.add(Mickeys(j['park_id'], j['land_id'], j['attraction_id'], j['photo_url'], j['description'], j['hint']))
		db.session.commit()
		return 'Done'

#Mickey by ID
@home_blueprint.route('/mickeys/<id>', methods=['GET', 'PUT', 'DELETE'])
def mickey_by_id(id):
	if request.method == 'GET':
		return jsonify(mickeys=[Mickeys.query.get(id).serialize()])
	if request.method == 'PUT':
		update = db.session.query(Mickeys).filter_by(id = id).update(request.json)
		db.session.commit()		
		return 'Done'
	if request.method == 'DELETE':
		m = Mickeys.query.get(id)
		db.session.delete(m)
		db.session.commit()
		return 'Done'	
								




