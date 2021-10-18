"""
Class map with some fun-ns
"""
class Map():
    """
    Create and refactor board
    """
    def __init__(self):
        """
        constructor
        """
        self.map = [i for i in range(1, 10)]

    def print_map(self):
        """
        print map
        :return:
        """
        for i in range(3):
            print('|', self.map[0 + i * 3], '|', self.map[1 + i * 3],\
                  '|', self.map[2 + i * 3], '|')
            print("-------------")
