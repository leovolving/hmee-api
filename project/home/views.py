from project import db
from project.models import Parks, Lands, Attractions
from flask import request, Blueprint, request
from flask.json import jsonify

home_blueprint = Blueprint(
    'home', __name__
) 

# use decorators to link the function to a url
@home_blueprint.route('/')
def home():
    return "Hello, World!"  # return a string


"""
PARKS TABLE
"""

@home_blueprint.route('/parks', methods=['GET'])
def parks():
	if request.method == 'GET':
		return jsonify(parks=[i.serialize() for i in Parks.query.all()])	


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
@home_blueprint.route('/attractions', methods=['GET'])
def attractions():
	if request.method == 'GET':
		return jsonify(attracitions=[i.serialize() for i in Attractions.query.all()])





				