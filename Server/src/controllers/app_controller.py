

class AppController():

	request = None

	def __init__(self, Game):
		self.db = Game.connection
		return

	def requester(self,request):
		self.request = request

	def output(self,text = None,newline = True):
		if newline:
			self.request.send(text+'\n\r')
		else:
			self.request.send(text)
