import time

class Admin():

	def __init__(self, Game):
		self.Game = Game
		return


	def init(self):
		print 'Admin initalised'
		print '> Type help'

		#self.cmd('create world')

		while True:
			cmd = raw_input(":");

			if cmd == 'quit' or cmd == 'q' or cmd == 'exit':
				print "See ya!"
				break
			else:
				self.Game.command.run(self, cmd)
				

	def send(self, text):
		print(text)


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




	def createPlayer(self):
		return



	def listEvents(self):
		for w in self.Game.connection.Event.find():
			print w['ticks']
		return
