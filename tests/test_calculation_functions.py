import unittest
from src.calculation_functions import calculate_monthly_fee, calculate_competition_fee
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestCalculationFunctions(unittest.TestCase):

    def test_calculate_monthly_fee(self):
        self.assertEqual(calculate_monthly_fee("Beginner"), 100.00)  # 4 weeks * £25.00
        self.assertEqual(calculate_monthly_fee("Intermediate"), 120.00)  # 4 weeks * £30.00
        self.assertEqual(calculate_monthly_fee("Elite"), 140.00)  # 4 weeks * £35.00

    def test_calculate_competition_fee_intermediate(self):
        self.assertEqual(calculate_competition_fee("Intermediate", 2), 44.00)  # 2 competitions

    def test_calculate_competition_fee_elite(self):
        self.assertEqual(calculate_competition_fee("Elite", 3), 66.00)  # 3 competitions

    def test_calculate_competition_fee_beginner(self):
        self.assertEqual(calculate_competition_fee("Beginner", 2), 0.0)  # Beginners can't enter competitions


if __name__ == '__main__':
    unittest.main()
