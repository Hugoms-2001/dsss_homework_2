import unittest
from math_quiz import random_number, random_symbol, operation


class TestMathGame(unittest.TestCase):

    def test_random_number(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_number(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_symbol(self):
        # Test if the symbol generated is one of '+', '-', or '*'
        for _ in range(100): # Test a large number of random values
            symbol = random_symbol()
            self.assertIn(symbol, ['+', '-', '*'])

    def test_operation(self):
        # Test if the function do correctly the operation
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (8, 3, '-', '8 - 3', 5),
            (4, 4, '*', '4 * 4', 16),
            (10, 0, '+', '10 + 0', 10),
            (7, 2, '*', '7 * 2', 14)
        ]

        for num1, num2, symbol, expected_problem, expected_solution in test_cases:
            problem, solution = operation(num1, num2, symbol)
            self.assertEqual(problem, expected_problem)   # Check if the operation format is correct
            self.assertEqual(solution, expected_solution)     # Check if the solution is correct


if __name__ == "__main__":
    unittest.main()
