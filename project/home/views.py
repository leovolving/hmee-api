from project import db
from project.models import Parks
from flask import request, Blueprint, request
from flask.json import jsonify

home_blueprint = Blueprint(
    'home', __name__
) 

# use decorators to link the function to a url
@home_blueprint.route('/')
def home():
    return "Hello, World!"  # return a string

@home_blueprint.route('/parks', methods=['GET'])
def parks():
	if request.method == 'GET':
		return jsonify(parks=[i.serialize() for i in Parks.query.all()])		       

@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template