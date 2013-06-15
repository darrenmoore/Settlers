from mongokit import Document, Connection

import datetime

class Player(Document):
	__collection__ = 'players'
	__database__ = 'players'

	structure = {
		'name': unicode,
		'username': basestring,
		'password': basestring,
		'created': datetime.datetime
	}

	required_fields = []

	default_values = {
	}

