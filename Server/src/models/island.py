from mongokit import Document, Connection
from models.world import World

from random import randint
from random import choice
import datetime

class Island(Document):
	__collection__ = 'islands'
	__database__ = 'islands'

	use_autorefs = True

	structure = {
		'name': basestring,
		'world': World,
		'player_id': int,
		'cells': list,
	}

	required_fields = []

	default_values = {
	}

	min_size = 20
	max_size = 50
	cell_size = 10	#100 spaces in a cell, 1 house takes up 2 cells

	_cells = []

	cell_resources = {
		'coal': 	{ 'min':5, 'max':50 },
		'lumber': 	{ 'min':5, 'max':50 },
		'stone': 	{ 'min':5, 'max':50 },
		'iron': 	{ 'min':5, 'max':50 },
		'gold' : 	{ 'min':5, 'max':50 }
	}



	def create(self, World):
		size = randint(self.min_size,self.max_size)

		self['name'] = 'Darrens Island!'
		self['world'] = World

		#Create first cell
		coords = self.findEmptyCell(World)
		self.addCell(coords)

		#Branch cell
		self.branchCell(coords, 0, size);

		#Continue building save data and save
		self['cells'] = self._cells
		self.save()

		#Add this cell to the world
		World['islands'].append(self)
		World.save()

		return


	def resources(self):

		totals = {}

		for r in self.cell_resources:
			totals[r] = 0

		for c in self['cells']:
			for r in c['resources']:
				total = c['resources'][r]
				totals[r] += total
				
		return totals;



	def addCell(self, coords):
		_resources = self.randomResources();

		save = {
			'x': coords['x'],
			'y': coords['y'],
			'size': self.cell_size,
			'resources': _resources
		}
		
		#Save to the world model
		self['world']['cells'][save['x']][save['y']] = 'hi'
		self['world'].save()

		#Add to a model scoped list to save to this model
		self._cells.append(save)

		return save



	def randomResources(self):
		r = {};
		resources = self.cell_resources
		for resource in resources:
			r[resource] = randint(resources[resource]['min'],resources[resource]['max'])
		return r;



	def branchCell(self, coords, depth = 0, max_depth = 0):
		n = self.emptyNeighbours(coords);

		#if no neighbours get out of here
		if not n:
			return depth

		randCoords = choice(n)
		self.addCell(randCoords)

		depth += 1
		if depth < max_depth:
			#either branch from random or these coords
			branchFrom = coords
			if randint(0,1):
				branchFrom = randCoords

			return self.branchCell(branchFrom, depth, max_depth);
		
		return depth



	def emptyNeighbours(self, coords):
		n = self.neighbours(coords)

		for cell in n:
			if not self.isEmptyCell(cell):
				n.remove(cell)
		return n


	def neighbours(self, coords):
		boundry = self['world']['size']
		n = [];

		#top
		for x in range(coords['x']-1,coords['x']+2):
			n.append({ 'x':x, 'y':coords['y']-1 })

		#bottom
		for x in range(coords['x']-1,coords['x']+2):
			n.append({ 'x':x, 'y':coords['y']+1 })

		#left and right
		n.append({ 'x':coords['x']-1, 'y':coords['y'] })
		n.append({ 'x':coords['x']+1, 'y':coords['y'] })

		#remove anything out of range
		output = [];
		for cell in n:
			if(cell['x'] >= 0 and cell['x'] < boundry and cell['y'] >= 0 and cell['y'] < boundry):
				output.append(cell)

		return output



	def isEmptyCell(self, coords):
		#Boundries
		boundry = self['world']['size']
		if(coords['x'] < 0 or coords['y'] < 0): return False
		if(coords['x'] > boundry-1): return False
		if(coords['y'] > boundry-1): return False

		cell = self['world']['cells'][coords['x']][coords['y']];
		if cell:
			return False;
		else:
			return True;



	def closestNeighbour(self, coords):
		#scipy.spatial.KDTree
		closest = 5;
		return closest;



	def findEmptyCell(self, World):
		while 1:
			x = randint(0,World['size']-1);
			y = randint(0,World['size']-1);

			if self.isEmptyCell({ 'x':x, 'y':y }) and self.closestNeighbour({ 'x':x, 'y':y }) > 4:
				return { 'x':x, 'y':y }
				break

		return