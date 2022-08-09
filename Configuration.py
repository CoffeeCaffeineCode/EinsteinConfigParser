# configuration class
class Configuration():
	def __init__(self, argv):
		for key, val in argv.items():
			self.__dict__[key] = val