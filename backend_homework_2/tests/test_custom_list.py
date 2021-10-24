"""
Test file
"""
import unittest
from custom_list import CustomList


class TestCustomList(unittest.TestCase):
    """
    Class for testing custom list
    """
    def setUp(self):
        """
        Create obj custom list
        :return:
        """
        self.custom_list = CustomList([0, 1, 2])
        self.test_data = [[1, 2, 3], [0, 1], [1, 2, 3, 4]]
        self.res_add = [[1, 3, 5], [0, 2, 2], [1, 3, 5, 4]]
        self.res_sub = [[-1, -1, -1], [0, 0, 2], [-1, -1, -1, -4]]
        self.res_rsub = [[1, 1, 1], [0, 0, -2], [1, 1, 1, 4]]

    def test_add_default_list(self):
        """
        test: <custom list> + <def list>
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertEqual(self.custom_list.__add__(self.test_data[item]), self.res_add[item])

    def test_radd_default_list(self):
        """
        test:  <def list> + <custom list>
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertEqual(self.custom_list.__radd__(self.test_data[item]), self.res_add[item])

    def test_isinstance_add(self):
        """
        test: new obj is instance CustomList after adding
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertIsInstance(self.custom_list.__add__(self.test_data[item]), CustomList)
            self.assertIsInstance(self.custom_list.__radd__(self.test_data[item]), CustomList)

    def test_sub_default_list(self):
        """
        test: <custom list> - <def list>
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertEqual(self.custom_list.__sub__(self.test_data[item]), self.res_sub[item])

    def test_rsub_default_list(self):
        """
        test:  <def list> - <custom list>
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertEqual(self.custom_list.__rsub__(self.test_data[item]), self.res_rsub[item])

    def test_isinstance_sub(self):
        """
        test: new obj is instance CustomList after sub
        :return:
        """
        for item in range(len(self.test_data)):
            self.assertIsInstance(self.custom_list.__sub__(self.test_data[item]), CustomList)
            self.assertIsInstance(self.custom_list.__rsub__(self.test_data[item]), CustomList)

    def test_eq_default(self):
        """
        test: sum(<list_1>) == sum(<list_2>)
        :return:
        """
        test_list = [0, 1, 2]
        self.assertEqual(self.custom_list.__eq__(test_list), True)

    def test_ne_default(self):
        """
        test: sum(<list_1>) != sum(<list_2>)
        :return:
        """
        test_list = [1, 1, 2]
        self.assertEqual(self.custom_list.__ne__(test_list), True)

    def test_le_default(self):
        """
        test: sum(<list_1>) <= sum(<list_2>)
        :return:
        """
        test_list = [[0, 1, 2], [1, 2, 3]]

        for item in test_list:
            self.assertEqual(self.custom_list.__le__(item), True)

    def test_lt_default(self):
        """
        test: sum(<list_1>) < sum(<list_2>)
        :return:
        """
        test_list = [4, 1, 2]
        self.assertEqual(self.custom_list.__lt__(test_list), True)

    def test_ge_default(self):
        """
        test: sum(<list_1>) >= sum(<list_2>)
        :return:
        """
        test_list = [[0, 1, 2], [1, 0, 0]]

        for item in test_list:
            self.assertEqual(self.custom_list.__ge__(item), True)

    def test_gt_default(self):
        """
        test: sum(<list_1>) > sum(<list_2>)
        :return:
        """
        test_list = [-1, -1, 0]
        self.assertEqual(self.custom_list.__gt__(test_list), True)

    def test_is_custom(self):
        """
        test: fun return copy (<custom list> / <def list>)
        :return:
        """
        test_list = [[0, 1, 2], CustomList([0, 1, 2])]

        for item in test_list:
            self.assertIsInstance(self.custom_list.is_custom(item), list)

    def test_add_for_full(self):
        """
        test: extend list for full
        :return:
        """
        test_list = [0, 1, 2, 3]
        self.assertEqual(self.custom_list.add_for_full(self.custom_list.current_list, test_list), [0, 1, 2, 0])