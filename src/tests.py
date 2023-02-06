import unittest

import pygame

from config import *
from dragger import Dragger
from move import Move
from piece import Piece
from position import Position
from sound import Sound


class MyTestCase(unittest.TestCase):
	def test_position(self):
		self.assertEqual(str(Position(0, 0)), 'a1')
		self.assertEqual(str(Position(1, 0)), 'b1')
		self.assertEqual(str(Position(2, 0)), 'c1')
		self.assertEqual(str(Position(3, 1)), 'd2')
		self.assertEqual(str(Position(4, 2)), 'e3')
		self.assertEqual(str(Position(5, 3)), 'f4')
		self.assertEqual(str(Position(6, 4)), 'g5')
		self.assertEqual(str(Position(7, 5)), 'h6')
	
	def test_piece(self):
		# Testing if the piece class works
		self.assertEqual(str(Piece(Position(0, 0))), 'a1')
		self.assertEqual(str(Piece(Position(1, 0))), 'b1')
		self.assertEqual(str(Piece(Position(2, 0))), 'c1')
		self.assertEqual(str(Piece(Position(3, 1))), 'd2')
		self.assertEqual(str(Piece(Position(4, 2))), 'e3')
		self.assertEqual(str(Piece(Position(5, 3))), 'f4')
		# Testing if each piece class works
		self.assertEqual(str(Piece(Position(0, 0), "w", "Pawn", 100)), 'wPawna1')
		self.assertEqual(str(Piece(Position(1, 0), "w", "Rook", 500)), 'wRookb1')
		self.assertEqual(str(Piece(Position(2, 0), "w", "Knight", 300)), 'wKnightc1')
		self.assertEqual(str(Piece(Position(3, 1), "w", "Bishop", 300)), 'wBishopd2')
		self.assertEqual(str(Piece(Position(4, 2), "w", "Queen", 900)), 'wQueene3')
	
	def test_config(self):
		# Testing if the config values are accessed correctly
		self.assertEqual(ROWS, 8)
		self.assertEqual(COLS, 8)
		self.assertEqual(WINDOW_SIZE, (800, 800))
		self.assertEqual(SQ_SIZE, 100)
		self.assertEqual(PIECE_SIZE, 50)
	
	def test_dragger(self):
		# Testing if the dragger class works
		dragger = Dragger()
		self.assertEqual(dragger.dragging, False)
		self.assertEqual(dragger.initial_piece, None)
		self.assertEqual(dragger.mouse_position, (0, 0))
		self.assertEqual(dragger.initial_position, None)
		self.assertEqual(dragger.mouse_board_position, Position(0, 0))
	
	def test_move(self):
		# Testing if the move class works
		move = Move(
			Piece(Position(0, 0), "w", "Pawn", 100),
			Piece(Position(1, 1), "b", "Pawn", 100)
			)
		self.assertEqual(str(move), 'a1 -> b2')
		self.assertEqual(move.start, Position(0, 0))
		self.assertEqual(move.end, Position(1, 1))
	
	def test_sound(self):
		pygame.init()
		# Testing if the sound class works
		sound = Sound("../assets/sounds/move.wav")
		# Assert if the sound is played
		sound.play()
		if sound.sound.get_num_channels() == 0:
			self.fail("Sound is not played")


if __name__ == '__main__':
	pygame.init()
	
	unittest.main()
