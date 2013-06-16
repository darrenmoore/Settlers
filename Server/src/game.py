import thread
import time

from mongokit import Document, Connection

from admin import *
from server import *
from ticker import *
from command import *

from controllers.worlds_controller import WorldsController
from controllers.helps_controller import HelpsController

from models.player import Player
from models.world import World
from models.island import Island
from models.event import Event


class Game():
	tickCount = 0

	def __init__(self):
		return

	def init(self):
		print('Game started')

		#Database connection
		self.database()

		#Controllers
		self.controllers();

		#Command
		self.command();

		#Game ticker
		thread.start_new_thread( self.ticker, () )

		#Server
		thread.start_new_thread( self.server, () )

		#Admin CLI
		time.sleep(1)
		self.admin()
		return



	def controllers(self):
		self.WorldsController = WorldsController(self)
		return


	#Database connection
	def database(self):
		print('Loading database')
		self.connection = Connection()
		self.connection.register([World])
		self.connection.register([Island])
		self.connection.register([Event])
		self.connection.register([Player])


	def admin(self):
		self.admin = Admin(self)
		self.admin.init()


	def server(self):
		self.server = Server(self)
		self.server.init()


	def ticker(self):
		self.ticker = Ticker(self)
		self.ticker.init()


	def command(self):
		self.command = Command(self)
		self.command.init()

