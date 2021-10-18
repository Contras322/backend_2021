"""
File for testing anything
"""
import unittest
from game import TicTacGame
from map import Map


class TestTicTacGame(unittest.TestCase):
    """
    Tests for TicTacGame class
    """
    def setUp(self):
        """
        Create obj game
        :return nothing:
        """
        self.game = TicTacGame

    def test_validate_input(self):
        """
        Test right input
        :return:
        """
        self.assertEqual(self.game.validate_input(self.game, '1'), 0)

    def test_raises(self):
        """
        Test wrong input
        :return:
        """
        self.assertRaises(TypeError, self.game.validate_input, self.game, 'asdfs')
        self.assertRaises(IndexError, self.game.validate_input, self.game, '123123')

    def test_draw(self):
        """
        Test draw game
        :return:
        """
        board = Map()
        board_for_draw = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        board.map = board_for_draw
        players = {'X': 'First', 'O': 'Second'}
        self.assertEqual(self.game.check_winner(self.game, players, count=9), False)
