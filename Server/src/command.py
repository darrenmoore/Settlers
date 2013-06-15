
class Command:

	commands = {
		'help': {}
	}

	def __init__(self, Game):
		self.Game = Game
		return


	def init(self):
		return


	def run(self, request, command):
		request.send('Command: "%s"\n\r' % command)
		return


	def help(self):
		return