"""
Test file
"""
import unittest
from custom_meta_class import CustomClass


class TestCustomMetaCLass(unittest.TestCase):
    """
    lass for testing custom meta class
    """
    def test_custom_val(self):
        """
        test custom val
        :return:
        """
        cust_1 = CustomClass()
        self.assertEqual(cust_1.custom_val, 99)

    def test_custom_line(self):
        """
        test custom line
        :return:
        """
        cust_2 = CustomClass()
        self.assertEqual(cust_2.custom_line(), 100)

    def test_custom_x(self):
        """
        test custom x
        :return:
        """
        cust_3 = CustomClass()
        self.assertEqual(getattr(cust_3, 'custom_x'), 50)

    def test_error_val(self):
        """
        test error
        :return:
        """
        cust_4 = CustomClass()
        with self.assertRaises(AttributeError):
            getattr(cust_4, 'val')

    def test_error_x(self):
        """
        test error x
        :return:
        """
        cust_5 = CustomClass()
        with self.assertRaises(AttributeError):
            getattr(cust_5, 'x')

    def test_error_line(self):
        """
        test error line
        :return:
        """
        cust_6 = CustomClass()
        with self.assertRaises(AttributeError):
            cust_6.line()
