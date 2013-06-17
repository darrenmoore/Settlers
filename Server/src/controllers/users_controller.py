from controllers.app_controller import AppController

class UsersController(AppController):


	def login(self):

		def password(input):
			print "Your password is "+input

		def username(input):
			self.output("Your username is "+input)
			self.input("Please enter your password", password)

		self.input('Please enter your username or type "n" to create a new user', username)


	def register(self):
		self.input('Enter a username', register_password)


	def register_password(self):
		self.output('Hello')

