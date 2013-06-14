from mongokit import Document, Connection

import datetime

class World(Document):
	__collection__ = 'worlds'
	__database__ = 'worlds'

	_map = []
	max_world_size = 40

	structure = {
		'name': basestring,
		'width': int,
		'height': int,
		'cells': list,
		'islands': list,
		'size': int
	}

	required_fields = []

	default_values = {
	}


	def create(self):
		self['name'] = 'Hey yo!2'
		self['size'] = self.max_world_size
		self['cells'] = self.cells()
		self.save()
		return self


	def cells(self): 
		del self._map[:]

		for rows in range(self.max_world_size):
			line = []
			for cols in range(self.max_world_size):
				line.append({});
			self._map.append(line);

		return self._map
