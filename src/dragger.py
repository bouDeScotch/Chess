import pygame

from config import *
from position import Position


class Dragger:
	
	def __init__(self):
		self.dragging = False
		self.initial_piece = None
		self.mouse_position = (0, 0)
	
	@property
	def initial_position(self):
		try:
			return self.initial_piece.position
		except AttributeError:
			return None
	
	@property
	def mouse_board_position(self):
		return Position(self.mouse_position[0] // SQ_SIZE, self.mouse_position[1] // SQ_SIZE)
	
	def update_mouse(self, event: pygame.event.Event):
		"""
		Update the mouse position. Is called when the mouse is moved.
		:param event: The event that is passed to the function
		:return:
		"""
		try:
			self.mouse_position = event.pos
		except AttributeError:
			pass
