"""
File with class for TicTacGame
"""
from map import Map


class TicTacGame:
    """
    Class for TicTacGame
    """
    def validate_input(self, value, board):
        """
        ValueError
        IndexError
        :return:
        """
        if not value.isdigit():
            raise TypeError('Wrong type')

        value = int(value)
        if value > 9 or value < 1:
            raise IndexError('Wrong index')

        if board.map[value] == 'X' or board.map[value] == 'O':
            raise ValueError('This cell is not free')
        return value



    def start_game(self):
        """
        Implementation of the game
        :return nothing:
        """
        count = 0
        players = {'X': '', 'O': ''}
        board = Map()

        players['X'] = input('Enter your name\n')
        players['O'] = input('Enter your name\n')

        board.print_map()
        while self.check_winner(board, players, count):
            if count % 2 != 0:
                value = input(f'{players["X"]}, your turn\n') - 1
                _x = self.validate_input(value, board)
                board.set_value(_x, 'X')
                board.print_map()
            else:
                value = input(f'{players["O"]}, your turn\n') - 1
                _o = self.validate_input(value, board)
                board.set_value(_o, 'O')
                board.print_map()

            count += 1

    def check_winner(self, board, players, count):
        """
        Checking the end of the game
        :return True or False:
        """
        if count == 9:
            print('Draw!!!')
            return False

        win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), \
                            (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8),)

        for comb in win_combinations:
            if board.map[comb[0]] == board.map[comb[1]] == board.map[comb[2]]:
                sym = board.map[comb[0]]
                print(f'{players[sym]} WIN')

                return False

        return True
