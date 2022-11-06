import unittest
from my_file_cod_2 import find_odds
from my_file_cod_2 import equals_or_not
from my_file_cod_2 import copy_function
from my_file_cod_2 import all_is_123
from my_file_cod_2 import create_tuple

class Test_2(unittest.TestCase):

    def test_not_contains(self):
        self.assertIsNot(9, find_odds([4, 2, 9, 18, 20]))

    def test_21(self):
        self.assertNotEqual(equals_or_not(5, 5), None)

    def test_same(self):
        self.assertIs(copy_function(7), 7)

    def test_123(self):
        self.assertIsNot(all_is_123(321), 321)

    def test_tuple(self):
        self.assertEqual(create_tuple([1, 2, 3, 4, 5], ['Вадим', 'Дмитрий', 'Марина', 'Екатерина', 'Максим']), \
                                [(1, 'Вадим'), (2, 'Дмитрий'), (3, 'Марина'), (4, 'Екатерина'), (5, 'Максим')])

    

if __name__ == '__main__':
    unittest.main()
