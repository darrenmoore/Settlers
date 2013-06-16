from controllers.app_controller import AppController

class WorldsController(AppController):


	def test(self):
		print('ok')
		return


	def create(self):
		#Create world
		collection = self.db.worlds
		world = collection.World()
		world.create()

		#Add islands to world
		collection = self.db.islands
		island = collection.Island()
		island.create(world)

		#print world
		for row in world['cells']:
			for col in row:
				if col:
					self.output('#',False)
				else:
					self.output('.',False)
			self.output('')

		#islands
		for island in world['islands']:
			self.output(island['name'])
			self.output('  total cells: '+str(len(island['cells'])))
			self.output('')

			#resources
			self.output('  Resources')
			self.output('  ----------------------')

			_resources = island.resources()
			for r in _resources:
				self.output('  '+r+': '+str(_resources[r]))


		return



		def list(self):
			for w in self.db.World.find():
				print w['name']
			return


		def show(self):
			w = self.db.World.find()
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
