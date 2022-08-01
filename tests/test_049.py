from unittest import TestCase

try:
    from problems.problem_049 import sum_two_numbers
except Exception:
    def sum_two_numbers(x, y): return None


class ProblemTests(TestCase):
    def test_sum(self):
        values = (1, 2)
        expected = 3
        result = sum_two_numbers(*values)
        self.assertEqual(
            expected,
            result,
            msg=f"The sum of {values} is {expected}"
        )
