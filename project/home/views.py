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
    return '<h1>HMEE API</h1> \
    <p>Visit <a href="https://github.com/Ljyockey/hmee-api" target="_blank">GitHub</a> for full documentation</p> \
	<h2 id="endpoints">Endpoints</h2> \
<p>Base URL: https://hmee-api.herokuapp.com</p> \
\
<h3 id="parks">Parks</h3> \
<p>DLR parks</p> \
<ul> \
	<li>GET: /parks - a list of all parks. <a href="/parks">Try now!</a></li> \
	<li>GET: /parks/:id - a single park by ID</li> \
</ul> \
\
<h3 id="lands">Lands</h3> \
<p>DLR lands, organized by park</p> \
<ul> \
	<li>GET: /lands - a list of all lands. <a href="/lands">Try now!</a></li> \
	<li>GET: /parks/:park_id/lands - a list of lands by park</li> \
	<li>GET: /lands:id - a single land by ID</li> \
</ul> \
\
<h3 id="attractions">Attractions</h3> \
<p>DLR attractions - organized by park and land</p> \
<ul> \
	<li>GET: /attractions - a list of all attractions. <a href="/attractions">Try now!</a></li> \
	<li>GET: /parks/:park_id/attractions - a list of attractions by park</li> \
	<li>GET: /lands/:land_id/attractions - a list of all attractions by land</li> \
	<li>GET: /attractions/:id - a single attraction by ID</li> \
</ul> \
\
<h3 id="mickeys">Mickeys</h3> \
<p>Hidden Mickeys and Easter Eggs. Referred henceforth as "Mickeys"</p> \
<ul> \
	<li>GET: /mickeys - a list of all Mickeys. <a href="/mickeys">Try now!</a></li> \
	<li>GET: /parks/:park_id/mickeys - list of Mickeys by park</li> \
	<li>GET: /lands/:land_id/mickeys - list of all Mickeys by land</li> \
	<li> GET: /attractions/:attraction_id/mickeys - list of all Mickeys by attraction</li> \
	<li>GET: lands/:land_id/mickeys/none - list of Mickeys by land where attraction_id = null</li> \
	<li>POST: /mickeys - add new row. *NOTE: content-type: application/json REQUIRED</li> \
	<li>PUT: /mickeys/:id - updates single row. *NOTE: content-type: application/json REQUIRED</li> \
	<li>DELETE: /mickeys/:id - deletes single row</li> \
</ul>'

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
		m = Mickeys(j['park_id'], j['land_id'], j['attraction_id'], j['photo_url'], j['description'], j['hint'])		
		db.session.add(m)
		db.session.commit()
		return jsonify({'mickey': m.serialize()}), 201

#Mickey by ID - GET/DELETE
@home_blueprint.route('/mickeys/<id>', methods=['GET', 'PUT', 'DELETE'])
def mickey_by_id(id):
	if request.method == 'GET':
		return jsonify(mickeys=[Mickeys.query.get(id).serialize()])

	if request.method == 'PUT':
		m = db.session.query(Mickeys).filter_by(id=id)
		m.update(request.json)	
		db.session.commit()		
		return 'Done', 204

	if request.method == 'DELETE':
		m = Mickeys.query.get(id)
		db.session.delete(m)
		db.session.commit()
		return 'Done', 204

#Mickeys by park
@home_blueprint.route('/parks/<park_id>/mickeys', methods=['GET'])
def mickeys_by_park(park_id):
	if request.method == 'GET':
		return jsonify(mickeys=[i.serialize() 
			for i in Mickeys.query.filter_by(park_id=park_id).all()])

#Mickeys by land
@home_blueprint.route('/lands/<land_id>/mickeys', methods=['GET'])
def mickeys_by_land(land_id):
	if request.method == 'GET':
		return jsonify(mickeys=[i.serialize() 
			for i in Mickeys.query.filter_by(land_id=land_id).all()])		

#Mickeys by attraction
@home_blueprint.route('/attractions/<attraction_id>/mickeys', methods=['GET'])
def mickeys_by_attraction(attraction_id):
	if request.method == 'GET':
		return jsonify(mickeys=[i.serialize() 
			for i in Mickeys.query.filter_by(attraction_id=attraction_id).all()])	

#Mickeys by land with no attraction
@home_blueprint.route('/lands/<land_id>/mickeys/none', methods=['GET'])
def mickeys_with_no_attraction(land_id):
	if request.method == 'GET':
		return jsonify(mickeys=[i.serialize() 
			for i in Mickeys.query.filter_by(land_id=land_id, attraction_id=None).all()])			
								




