import unittest
from game import TicTacGame


class TestValidateInput(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame

    def test_input(self):
        board_for_draw = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        players = {'X': 'First', 'O': 'Second'}
        self.assertEqual(self.game.check_winner(board_for_draw, players, count=9), False)


