
from controllers.helps_controller import HelpsController
from controllers.worlds_controller import WorldsController


class Command:

	routes = {
		'help': { 'controller':HelpsController, 'method':'show' },
		'create world': { 'controller':WorldsController, 'method':'create' },
	}

	def __init__(self, Game):
		self.Game = Game
		return


	def init(self):
		return


	def run(self, request, command):
		request.send('Command: "%s"\n\r' % command)

		if command not in self.routes:
			print('Unknown command')
			return

		route = self.routes[command]
		controller = route['controller'](self.Game)

		controller.requester(request)
		getattr(controller, route['method'])()

