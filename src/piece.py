from typing import Literal

from position import Position


class Piece:
	
	def __init__(
			self, position: Position, color: Literal["w", "b", ""] = "", name: str = "",
			value: int = 0
			):
		self.position = position
		self.color = color
		self.name = name
		self.value = value
		self.has_moved = False
		self.just_moved = False
	
	def get_moves(self, board):
		# TODO: Implement this
		pass
	
	def __str__(self):
		return f"{self.color}{self.name}{self.position}"
	
	def __repr__(self):
		return self.__str__()


class Pawn(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "Pawn", 100)


class Rook(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "Rook", 500)


class Knight(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "Knight", 300)


class Bishop(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "Bishop", 300)


class Queen(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "Queen", 900)


class King(Piece):
	def __init__(self, position: Position, color: Literal["w", "b"]):
		super().__init__(position, color, "King", 10000)
