"""
File with class for TicTacGame
"""

class TicTacGame:
    """
    Class for TicTacGame
    """


    def show_board(board):
        """
        Print board
        :param board:
        :return nothing:
        """
        for i in range(3):
            print('|', board[0 + i * 3], '|', board[1 + i * 3],\
                  '|', board[2 + i * 3], '|')
            print("-------------")


    def validate_input(value):
        """
        ValueError
        IndexError
        :return:
        """
        try:
            if value.isdigit():
                value = int(value)
                if value > 8 or value < 0:
                    raise IndexError
                else:
                    return value
            else:
                raise ValueError

        except ValueError:
            print('Wrong value')
            exit()

        except IndexError:
            print('Wrong index')
            exit()


    def start_game(self):
        """
        Implementation of the game
        :return nothing:
        """
        count = 0
        players = {'X': '', 'O': ''}
        board = [i for i in range(9)]

        players['X'] = input('Enter your name\n')
        players['O'] = input('Enter your name\n')

        self.show_board(board)
        while self.check_winner(board, players, count):
            if count % 2 != 0:
                value = input('{}, your turn\n'.format(players['X']))
                _x = self.validate_input(value)
                board[_x] = 'X'
                self.show_board(board)
            else:
                value = input('{}, your turn\n'.format(players['O']))
                _o = self.validate_input(value)
                board[_o] = 'O'
                self.show_board(board)

            count += 1


    def check_winner(board, players, count):
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
            if board[comb[0]] == board[comb[1]] == board[comb[2]]:
                sym = board[comb[0]]
                print('{} WIN'.format(players[sym]))

                return False

        return True
