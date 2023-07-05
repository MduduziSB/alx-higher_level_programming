#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer
"""Class TestMax_Integer"""


class TestMaxInteger(unittest.TestCase):
    """Class used to test max_integer function"""
    def test_none_empty_list(self):
        """arguments"""
        list_t = [0, -1, 5, 4]
        """test"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, 5)

    def test_empty_list(self):
        """Setup"""
        list_t = []
        """Action"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, None)

    def test_float_numbers(self):
        """setup"""
        list_t = [0.01, 0.009, -0.2]
        """test"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, 0.01)

    def test_float_int_numbers(self):
        """setup"""
        list_t = [0.01, -7, 1]
        """test"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, 1)

    def test_strings_list(self):
        """setup"""
        list_t = ["owk", "awesome", "cool"]
        """test"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, "owk")

    def test_string(self):
        """setup"""
        string = "mduduzi"
        """test"""
        result = max_integer(string)
        """Make assertion"""
        self.assertEqual(result, 'z')

    def test_one_numbers(self):
        """setup"""
        list_t = [-0.2]
        """test"""
        result = max_integer(list_t)
        """Make assertion"""
        self.assertEqual(result, -0.2)

    if __name__ == '__main__':
        unittest.main()
