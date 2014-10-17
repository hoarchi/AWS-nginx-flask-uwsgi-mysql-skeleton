class Config(object):
	SECRET_KEY = "aaaaaaa"
	debug = False


class Production(Config):
	debug = True
	CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = "mysql://username:password@000.000.000.000/DBname"
	migration_directory = "migrations"
