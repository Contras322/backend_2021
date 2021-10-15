import unittest
from game import TicTacGame
from map import Map


class TestValidateInput(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame

    def test_input(self):
        board = Map()
        self.assertEqual(self.game.validate_input(self.game, '1', board), 1)

    def test_raises(self):
        board = Map()
        self.assertRaises(TypeError, self.game.validate_input, self.game, 'asdfs', board)

    def test_draw(self):
        board_for_draw = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        players = {'X': 'First', 'O': 'Second'}
        self.assertEqual(self.game.check_winner(self.game, board_for_draw, players, count=9), False)
