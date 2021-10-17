"""
File with class for TicTacGame
"""
from map import Map


class TicTacGame:
    """
    Class for TicTacGame
    """
    board = Map()

    def validate_input(self, value):
        """
        ValueError
        IndexError
        :return:
        """
        if not value.isdigit():
            raise TypeError

        value = int(value) - 1
        if value > 8 or value < 0:
            raise IndexError

        if self.board.map[value] == 'X' or self.board.map[value] == 'O':
            raise ValueError

        return value

    def handing_errors(self, value):
        """
        Handing some errors
        :param value:
        :return:
        """
        try:
            value = self.validate_input(value)
        except IndexError:
            print('Wrong index')
        except ValueError:
            print('This cell is not free')
        except TypeError:
            print('Wrong type')
        else:
            return value

        exit()
        return None

    def start_game(self):
        """
        Implementation of the game
        :return nothing:
        """
        count = 0
        players = {'X': '', 'O': ''}
        syms = ['X', 'O']

        players['X'] = input('Enter your name\n')
        players['O'] = input('Enter your name\n')

        self.board.print_map()
        while self.check_winner(players, count):
            value = input(f'{players[syms[count % 2]]}, your turn\n')
            self.board.set_value(self.handing_errors(value), syms[count % 2])
            self.board.print_map()

            count += 1

    def check_winner(self, players, count):
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
            if self.board.map[comb[0]] == self.board.map[comb[1]] == self.board.map[comb[2]]:
                sym = self.board.map[comb[0]]
                print(f'{players[sym]} WIN')

                return False

        return True
