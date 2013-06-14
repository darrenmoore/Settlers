import time

class Admin():

	def __init__(self, Game):
		self.Game = Game
		return


	def init(self):
		print 'Admin initalised'
		print '> Type help'

		self.createWorld()

		while True:
			cmd = raw_input(":");

			if cmd == 'quit' or cmd == 'q' or cmd == 'exit':
				print "See ya!"
				break
			elif cmd == 'ticks':
				print 'Ticks elapsed: '+str(self.Game.ticker.ticks())
			elif cmd == 'list worlds':
				self.listWorlds()
			elif cmd == 'list events':
				self.listEvents()
			elif cmd == 'show world':
				self.showWorld()
			elif cmd == 'create world':
				self.createWorld()
			#elif cmd == 'create player':
		return


	def listWorlds(self):
		for w in self.Game.connection.World.find():
			print w['name']
		return


	def showWorld(self):
		w = self.Game.connection.World.find()
		cells = w['cells']

		for row in cells:
			for col in row:
				if col:
					print('#'),
				else:
					print('.'),
			print
		return;

		return;


	def createWorld(self):
		#Create world
		collection = self.Game.connection.worlds
		world = collection.World()
		world.create()

		#Add islands to world
		collection = self.Game.connection.islands
		island = collection.Island()
		island.create(world)

		#print world
		for row in world['cells']:
			for col in row:
				if col:
					print('#'),
				else:
					print('.'),
			print

		#islands
		for island in world['islands']:
			print island['name']
			print '  total cells: '+str(len(island['cells']))
			print

			#resources
			print '  Resources'
			print '  ----------------------'
			_resources = island.resources()
			for r in _resources:
				print '  '+r+': '+str(_resources[r])


		return


		#self.Game.connection.worlds.insert({ 'name':'arse' })
		print "Created new world"
		return


	def createPlayer(self):
		return



	def listEvents(self):
		for w in self.Game.connection.Event.find():
			print w['ticks']
		return
