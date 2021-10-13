import unittest
from game import TicTacGame


class TestValidateInput(unittest.TestCase):
    def setUp(self):
        self.game = TicTacGame

    def test_input(self):
        self.assertEqual(self.game.validate_input('1'), 1)
        self.assertEqual(self.game.validate_input('8'), 8)
        self.assertEqual(self.game.validate_input('0'), 0)


