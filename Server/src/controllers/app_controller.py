

class AppController():

	request = None

	def __init__(self, Game):
		self.db = Game.connection
		self.Game = Game
		return


	def requester(self,request):
		self.request = request


	def output(self,text = None,newline = True):
		if newline:
			self.request.send(text+'\n\r')
		else:
			self.request.send(text)


	def input(self, text, callback):
		self.Game.command.hook(callback)
		self.output(text)

