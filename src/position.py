class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __str__(self):
		# return an algebraic notation of the position (e.g. a1, b2, c3, etc.)
		return chr(self.x + 97) + str(self.y + 1)
	
	def __repr__(self):
		return self.__str__()
	
	def __eq__(self, other):
		try:
			return self.x == other.position.x and self.y == other.position.y
		except AttributeError:
			return self.x == other.x and self.y == other.y
