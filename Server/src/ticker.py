import time

class Ticker():
	tickCount = 0

	def __init__(self, Game):
		self.Game = Game
		return


	def init(self):
		print 'Ticker initalised'

		while True:
			self.tickCount += 1;
			self.events();
			time.sleep( 1 );
		return


	def ticks(self):
		return self.tickCount


	def events(self):
		#print 'Events'
		return