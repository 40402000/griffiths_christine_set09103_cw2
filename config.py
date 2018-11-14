import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:

	SECRET_KEY = os.environ.get('\xa5\x11\x06\x03q\xb4\xe5\x08o\xdb\xba9\x8fxT\xa9\xf6\xe6\x1bi\tW\x03\xd6')
	SQLALCHEMY_TRACK_MODIFICATION = False
	
	@staticmethod
	def init_app(app):
		pass

class DevelopmentConfig(Config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI =\
    		'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestConfig(Config):
	TESTING = True
	SQLALCHEMY_DATABASE_URI =\
                'sqlite:///' 
### different database for testing avoids accidental overwrites ###

config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	### eventual production config here ###
	
	'default': Development
}
