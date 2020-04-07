
from . import webapp

@webapp.cli.command('init_db')
def init_db():
	""" Create an empty database. """
	# connect_db
	# excute schema.sql