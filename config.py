import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI=os.environ['DATABASE_URL']
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
	DEBUG = True
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

class DevelopmentConfig(Config):
	DEBUG = True

class ProductionConfig(Config):
	DEBUG = False		