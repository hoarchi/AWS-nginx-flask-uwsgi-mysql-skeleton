class Config(object):
	SECRET_KEY = "aaaaaaa"
	debug = False


class Production(Config):
	debug = True
	CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = "mysql://username:password@127.0.0.1/DBname"
	migration_directory = "migrations"
