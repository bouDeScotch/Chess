from piece import Piece


class Move:
	
	def __init__(self, start: Piece, end: Piece):
		self.start = start
		self.end = end
	
	def get_eval(self):
		# TODO : check if accurate later
		return self.end.value - self.start.value
	
	@property
	def litteral_positions(self):
		return str(self.start.position), str(self.end.position)
	
	def __str__(self):
		start, end = self.litteral_positions
		return f"{start} -> {end}"
	
	def __repr__(self):
		return self.__str__()
	
	def __eq__(self, other):
		return self.start == other.start and self.end == other.end

