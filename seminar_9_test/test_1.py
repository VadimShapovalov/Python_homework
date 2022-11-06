
import unittest
from my_file_cod_1 import sum_odd_position
from my_file_cod_1 import sum_mult
from my_file_cod_1 import Is_square
from my_file_cod_1 import find_even
from my_file_cod_1 import check_odd

class Test_1(unittest.TestCase):
    
    def test_equal(self):
        self.assertEqual(sum_odd_position([1, 2, 3, 4 , 5, 6]), 9)


    def test_equal_2(self):
        self.assertEqual(sum_mult(5), [1, 2, 6, 24, 120])

    def test_check_true(self):
        self.assertTrue(Is_square(5, 5), True)

    def test_contains(self):
        self.assertIn(6, find_even([1, 5, 33, 6, 21]))

    def test_None(self):
        self.assertIsNone(check_odd(6))

if __name__ == '__main__':
    unittest.main()
