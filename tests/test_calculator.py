import unittest

from src import calculator


class calculator_test(unittest.TestCase):

    def test_sum(self):
        assert calculator.sum(2,3) == 5

    def test_sub(self):
        assert calculator.sub(10,5) == 5

    def test_multiplication(self):
        assert calculator.multiplication(10,10) == 100

    def test_division(self):
        try:
            assert calculator.division(10,2) == 5
        except ZeroDivisionError as e:
            print("no se puede dividir entre zero", e)

