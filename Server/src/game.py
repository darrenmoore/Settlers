import thread
import time

from mongokit import Document, Connection

from admin import *
from server import *
from ticker import *

from models.world import World
from models.island import Island
from models.event import Event

connection = False


class Game():
	tickCount = 0

	def __init__(self):
		return

	def init(self):
		print 'Game started';

		#Database connection
		self.database()

		#Game ticker
		thread.start_new_thread( self.ticker, () )

		#Server
		thread.start_new_thread( self.server, () )

		#Admin CLI
		time.sleep(1)
		self.admin()
		return


	#Database connection
	def database(self):
		print 'Loading database'
		self.connection = Connection()
		self.connection.register([World])
		self.connection.register([Island])
		self.connection.register([Event])
		return


	def admin(self):
		#Admin CLI
		self.admin = Admin(self)
		self.admin.init()
		return


	def server(self):
		self.server = Server(self)
		self.server.init()
		return


	def ticker(self):
		self.ticker = Ticker(self)
		self.ticker.init()
		return




