# import the Flask class from the flask module
from flask import Flask, render_template, request
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# create the application object
app = Flask(__name__)


#config
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
print(app.config['SQLALCHEMY_DATABASE_URI'])

class Parks(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)

	def serialize(self):
		return {
			'id': self.id,
			'name': self.name
		}


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/parks', methods=['GET'])
def parks():
	if request.method == 'GET':
		return jsonify(parks=[i.serialize() for i in Parks.query.all()])		       

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()