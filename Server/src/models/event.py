from mongokit import Document, Connection

import datetime

class Event(Document):
	__collection__ = 'events'
	__database__ = 'events'

	structure = {
		'ticks': int,
		'repeat': bool,
		'method': basestring,
		'options': dict
	}

	required_fields = []

	default_values = {
	}

