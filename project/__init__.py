# import the Flask class from the flask module
from flask import Flask
from flask.json import jsonify
from flask_sqlalchemy import SQLAlchemy
import os

# create the application object
app = Flask(__name__)


#config
app.config.from_object(os.environ['APP_SETTINGS'])
print(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from project.home.views import home_blueprint

app.register_blueprint(home_blueprint)