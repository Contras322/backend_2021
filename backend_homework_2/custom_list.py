"""
File with class CustomList
"""
class CustomList(list):
    """
    Class CustomList with methods
    """
    def __init__(self, current_list):
        """
        init
        :param current_list:
        """
        self.current_list = current_list

    def __add__(self, other):
        """
        plus method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if len(self.current_list) < len(other_list):
            left_list = self.add_for_full(self.current_list, other_list)
            right_list = other_list

        elif len(self.current_list) > len(other_list):
            left_list = self.add_for_full(other_list, self.current_list)
            right_list = self.current_list[:]

        else:
            left_list = self.current_list[:]
            right_list = other_list

        new_custom_list = []
        for i in range(len(left_list)):
            new_custom_list.append(left_list[i] + right_list[i])

        final_list = CustomList(new_custom_list)

        return final_list

    def __radd__(self, other):
        """
        right plus method
        :param other:
        :return:
        """

        return self + other

    def __sub__(self, other):
        """
        minus method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if len(self.current_list) < len(other_list):
            left_list = self.add_for_full(self.current_list, other_list)
            right_list = other_list

        elif len(self.current_list) > len(other_list):
            left_list = self.current_list[:]
            right_list = self.add_for_full(other_list, self.current_list)

        else:
            left_list = self.current_list[:]
            right_list = other_list

        new_custom_list = []
        for i in range(len(right_list)):
            new_custom_list.append(left_list[i] - right_list[i])

        final_list = CustomList(new_custom_list)

        return final_list

    def __rsub__(self, other):
        """
        right minus method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if len(self.current_list) < len(other_list):
            left_list = self.add_for_full(self.current_list, other_list)
            right_list = other_list

        elif len(self.current_list) > len(other_list):
            left_list = self.current_list[:]
            right_list = self.add_for_full(other_list, self.current_list)

        else:
            left_list = self.current_list[:]
            right_list = other_list

        new_custom_list = []
        for i in range(len(right_list)):
            new_custom_list.append(right_list[i] - left_list[i])

        final_list = CustomList(new_custom_list)

        return final_list

    def __eq__(self, other):
        """
        == method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) == sum(other_list):
            return True

        return False

    def __lt__(self, other):
        """
        < method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) < sum(other_list):
            return True

        return False

    def __le__(self, other):
        """
        <= method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) <= sum(other_list):
            return True

        return False

    def __ne__(self, other):
        """
        != method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) != sum(other_list):
            return True

        return False

    def __gt__(self, other):
        """
        > method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) > sum(other_list):
            return True

        return False

    def __ge__(self, other):
        """
        >= method
        :param other:
        :return:
        """
        other_list = self.is_custom(other)

        if sum(self.current_list) >= sum(other_list):
            return True

        return False

    def add_for_full(self, short, long):
        """
        add some zeros
        :param short:
        :param long:
        :return:
        """
        new_list = [0] * (len(long) - len(short))
        new_current_list = short
        new_current_list = new_current_list + new_list

        return new_current_list

    def is_custom(self, other):
        """
        checking custom
        :param other:
        :return:
        """
        if isinstance(other, CustomList):
            other_list = other.current_list[:]

        else:
            other_list = other[:]

        return other_list
