from generic_backend import GenericBackend

class Database(GenericBackend):
	def __init__(self, username, password, host, 
				port, table, col_login, col_password, 
				hash=None):
		"""
			Initializes database object
		"""
		self.db_username = username
		self.db_password = password
		self.db_host = host
		self.db_port = port
		self.connect()

	class connect(self):
		""" 
			Connects to the database
		"""
		pass

	class disconnect(self):
		""" 
			Disconnects from the database
		"""
		pass		
