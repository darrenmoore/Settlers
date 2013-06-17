from controllers.app_controller import AppController

class HelpsController(AppController):


	def show(self):
		self.output('User help -----')


	def admin_show(self):
		self.output('Admin help -----')