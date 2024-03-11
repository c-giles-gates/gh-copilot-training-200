import unittest
from loan_calculator import calculate_amortization

class TestLoanCalculator(unittest.TestCase):
    def test_calculate_amortization_1(self):
        self.assertAlmostEqual(calculate_amortization(100000, 5, 30), 536.82, places=2)

    def test_calculate_amortization_2(self):
        self.assertAlmostEqual(calculate_amortization(200000, 3.92, 15), 1475.61, places=2)

    def test_calculate_amortization_3(self):
        self.assertAlmostEqual(calculate_amortization(350000, 4.5, 30), 1771.16, places=2)

    def test_calculate_amortization_4(self):
        self.assertAlmostEqual(calculate_amortization(500000, 3.75, 15), 3636.10, places=2)

    def test_calculate_amortization_5(self):
        self.assertAlmostEqual(calculate_amortization(750000, 2.67, 10), 7119.29, places=2)

if __name__ == '__main__':
    unittest.main()